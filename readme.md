<div id="top"></div>

<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SalMireles/simple-booking-api">
    <img src="images/hotel.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Booking API</h3>

  <p align="center">
    Want to book a room?
    <br />
    <a href="https://github.com/SalMireles/simple-booking-api"><strong>Check in »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/SalMireles/simple-booking-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/SalMireles/simple-booking-api/issues">Request Feature</a>
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
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a simple api to book hotel rooms.

##### Architecture Info
- Hotels
  - Layered: Database (db) --> Operations --> Routers
  - Database defines the models and creates sessions, and initializes the database with data
  - Operations uses the database models to perform operations (e.g compute prices)
  - Routers used operations to perform tasks, handles authentication, and routes endpoints

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

  [![Flask][flask-shield]][flask-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python 3.10.0 via pyenv
  ```sh
  pyenv install 3.10.0
  ```

### Installation

1. Get a private API Key (contact Sal)
2. Clone the repo
   ```sh
   git clone https://github.com/SalMireles/simple-booking-api
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Install packages and boot virtual environment
   ```make
   make install
   ```
2. Boot the app server using uvicorn
   ```make
   make run
   ```
3. Get endpoint
   ```make
   make get endpoint=""
   make get endpoint="rooms"
   make get endpoint="room/2"
   ```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Define API Models
- [x] Create layered architecture scaffold
- [ ] Add bookings router and add operations for room bookings

See the [open issues](https://github.com/SalMireles/simple-booking-api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Awesome README](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [Creating SQLite Test DB](https://www.quackit.com/sqlite/tutorial/create_a_relationship.cfm)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- https://github.com/Ileriayo/markdown-badges -->

[issues-shield]: https://img.shields.io/github/issues/SalMireles/simple-booking-api.svg?style=for-the-badge

[issues-url]: https://github.com/SalMireles/simple-booking-api/issues

[license-shield]: https://img.shields.io/github/license/SalMireles/simple-booking-api.svg?style=for-the-badge

[license-url]: https://github.com/SalMireles/simple-booking-api/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/salvador-mireles-b64908123/

[product-screenshot]: images/cloud.jpg

[flask-shield]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white

[flask-url]: https://flask.palletsprojects.com/en/2.1.x/

