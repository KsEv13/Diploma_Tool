<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Machine Learning-based Tool for Automated Proficiency Level
Determination of Developers based on their GitHub Profiles</h3>

  <p align="center">
    This tool can provide a valuable assistance during an estimation of programmers' skills. 
    It automatically estimates the level of qualifications (Junior/Middle/Senior) based on provided GitHub profile.
    <br />
    <a href="https://github.com/KsEv13/Diploma_Tool"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KsEv13/Diploma_Tool">View Demo</a>
    ·
    <a href="https://github.com/KsEv13/Diploma_Tool/issues">Report Bug</a>
    ·
    <a href="https://github.com/KsEv13/Diploma_Tool/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
This tool was developed as a thesis work "Machine Learning-based Tool for Automated Proficiency Level Determination of Developers based on their GitHub Profiles". 
The KNN model scored the highest on the macro F1-score, which is why the KNN model is used in this tool. 
The tool receives only the GitHub name as input and the output is a model-defined level.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][Flask.com]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
Will be changed in the next commit
* sklearn
* flask
* requests
* datetime
* json
* bs4
* nltk.stem
* re
* pandas
* time

  ```sh
  npm install flask@latest -g
  ```

### Installation

1. Get a free GitHub Token as shown in the [instruction](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?ref=maddhruv)
2. Clone the repo
   ```sh
   git clone https://github.com/KsEv13/Diploma_Tool.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your GitHub token in `main.py`
   ```py
   github_token = 'ENTER YOUR GITHUB TOKEN';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Demo will be added in the next commit

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Automated qualification level detection of developers based on their GitHub profiles

See the [open issues](https://github.com/KsEv13/Diploma_Tool/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Kseniya Evdokimova - k.evdokimova@innopolis.university
Amina Khusnutdinova - a.khusnutdinova@innopolis.university
Project Link: [https://github.com/KsEv13/Diploma_Tool](https://github.com/KsEv13/Diploma_Tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/KsEv13/Diploma_Tool.svg?style=for-the-badge
[forks-url]: https://github.com/KsEv13/Diploma_Tool/network/members
[stars-shield]: https://img.shields.io/github/stars/KsEv13/Diploma_Tool.svg?style=for-the-badge
[stars-url]: https://github.com/KsEv13/Diploma_Tool/stargazers
[issues-shield]: https://img.shields.io/github/issues/KsEv13/Diploma_Tool.svg?style=for-the-badge
[issues-url]: https://github.com/KsEv13/Diploma_Tool/issues
[product-screenshot]: images/screenshot.png

[Flask.com]: https://img.shields.io/badge/%20-Flask-red
[Flask-url]: https://flask.palletsprojects.com/en/latest/
