from datetime import datetime
import json
from bs4 import BeautifulSoup

from get_response import get_response
from is_good_commit_message import is_good_commit_message


class User:

    def __init__(self, username):
        self.username = username
        self.organizations_count = 0
        self.followers = 0
        self.repositories_count = 0
        self.projects_count = 0
        self.stars = 0
        self.forks = 0
        self.languages = {}
        self.languages_count = 0
        self.repositories_for_3_popular_languages_count = 0
        self.registration_date = None
        self.registered_days = 0
        self.contributions = 0
        self.get_user_organization()
        self.get_user_followers()
        self.get_user_repositories()
        self.get_user_projects()
        self.get_user_languages()
        self.get_user_languages_count()
        self.get_user_repositories_for_3_popular_languages_count()
        self.get_user_registration_date()
        self.get_user_registered_days()
        self.get_user_contributions()
        self.get_user_forks()
        self.get_user_stars()

    #  Функция для получения списка организаций, связанных с пользователем GitHub
    def get_user_organization(self):
        endpoint_url = f"users/{self.username}/orgs"
        
        print('USERNAME: ', self.username)
        organizations = get_response(endpoint_url=endpoint_url)

        # organizations = [i['login'] for i in organizations]
        self.organizations_count = len(organizations)


    def get_user_followers(self):
        endpoint_url = f"users/{self.username}/followers"
        self.followers = len(get_response(endpoint_url=endpoint_url))       

    # Функция для получения всех репозиториев пользователя на GitHub
    def get_user_repositories(self):
        endpoint_url = f"users/{self.username}/repos"
        self.repos = get_response(endpoint_url=endpoint_url)
        self.repositories_count = len(self.repos)

    # Функция для получения проектов пользователя на GitHub
    def get_user_projects(self):
        endpoint_url = f"users/{self.username}/projects"
        self.progects = get_response(endpoint_url=endpoint_url)
        self.projects_count = len(self.progects)

    def get_user_stars(self):
        stars = 0
        for repo in self.repos:
            stars += int(repo["stargazers_count"])
        self.stars = stars

    def get_user_forks(self):
        forks = 0
        for repo in self.repos:
            forks += int(repo["forks"])
        self.forks = forks

    #  Функция для получения словаря языков программирования пользователя GitHub
    #  И количество репозиториев, в которых эти языки были использованы
    def get_user_languages(self):
        languages = {}
        for repo in self.repos:
            endpoint_url = repo["languages_url"]
            languages_in_repo = get_response(endpoint_url=endpoint_url)
            for lang in languages_in_repo:
                if lang in languages:
                    languages[lang] += 1
                else:
                    languages[lang] = 1
        self.languages = languages

    # Функция для определения количества всех используемых пользователем языков
    def get_user_languages_count(self):
        self.languages_count = len(self.languages)

    # Функция для определения количества репозиториев,
    # написанных на 3 самых часто-испольуемых пользователем языков
    def get_user_repositories_for_3_popular_languages_count(self):
        # Exclude Markdown language from consideration
        self.languages.pop('Markdown', None)

        # Sort the languages by the number of repositories in descending order
        sorted_languages = sorted(self.languages.items(), key=lambda x: x[1], reverse=True)

        # Extract the top three most used languages
        top_languages = sorted_languages[:3]
        print('top_languages: ', top_languages)

        # Assign the languages to variables
        first_language = top_languages[0][1] if len(top_languages) >= 1 else 0
        second_language = top_languages[1][1] if len(top_languages) >= 2 else 0
        third_language = top_languages[2][1] if len(top_languages) >= 3 else 0

        self.repositories_for_3_popular_languages_count = first_language + second_language + third_language
    
    #  Функция для получения даты регистрации пользователя GitHub
    def get_user_registration_date(self):
        endpoint_url = f"users/{self.username}"
        self.registration_date = get_response(endpoint_url=endpoint_url)['created_at']

    #  Функция для получения даты регистрации пользователя GitHub
    def get_user_registered_days(self):
        if self.registration_date == None:
            self.registered_days = 0
        reg_date_standard = datetime.strptime(str(self.registration_date), '%Y-%m-%dT%H:%M:%SZ')
        self.registered_days = (datetime.now() - reg_date_standard).days
    
    # Функция для получения вкладов пользователя на GitHub
    def get_user_contributions(self):
        GITHUB_URL = 'https://github.com/'
        url = f'{GITHUB_URL}{self.username}'

        response = get_response(endpoint_url=url, return_json = False)

        bs = BeautifulSoup(response.content, "html.parser")
        total = bs.find('div', {'class': 'js-yearly-contributions'}).findNext('h2')
        contributions = int(total.text.split()[0].replace(',', ''))

        self.contributions = json.dumps(contributions, indent=4)

    def get_user_commit_data(self):

        total_commits_number = 0
        good_message_commits = 0

        for repo in self.repos:

            repo_name = repo["name"]
            commits_endpoint_url = f"repos/{self.username}/{repo_name}/commits"
            repo_commits = get_response(endpoint_url=commits_endpoint_url)

            # Проходимся по коммитам и анализируем содержимое файлов
            for commit in repo_commits:

                if commit["commit"]["author"]["name"] == self.username:
                    total_commits_number += 1

                    commit_message = commit["commit"]["message"]

                    if is_good_commit_message(commit_message):
                        good_message_commits += 1

                    commit_url = commit["url"]
                    commit_url_response = get_response(endpoint_url=commit_url)

                    commit_files = commit_url_response["files"]
                    
                    for file in commit_files:
                        file_name = file["filename"]

        self.good_commit_messages_ratio = good_message_commits / total_commits_number


# user = User('Amina19058')
