# NEWS APP

#### A Python web application which shows news articles from various sources using the News API

![Description](app.png)

#### Live link:https://news-app11.herokuapp.com/

## Description

An application which shows news articles from various sources using the [News API](https://newsapi.org/), it is made by python web framework, Flask.

## User Stories

- A user I can view various news sources on the homepage of the application.
- A user can select a news source and see all news articles from the selected news source in the application.
- A user can search for a news article on the homepage.
- A user can see the image, description,author and the time a news article was created.
- A can click on an article and read the full article on the source website.

## Behaviour Driven Development (BDD)

| Behaviour                                                                                        |                                                                      Input                                                                       |                                                                                                 Output |
| ------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------------------------: |
| Page loads, user arrives in the landing page, a list of all available news sources is displayed. | The user can click on any particular list group item to be directed to a separate page containing news highlights curated by the same publisher. | On clicking the "read more" button, the user is redirected to the main article to read the full story. |  |

## Features

Here are the summary:

- A landing page showing top world headline news and search bar.
- Clickable news sources which direct the user to a page with article highlights from the particular source.
- Clickable news articles which direct the user to the source website to read full article details

## Requirements

- This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)

##### Contribution

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/HASSAN1A/News-App/issues/new) by including your search query and the expected result.
If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/HASSAN1A/News-App). Please include sample queries and their corresponding results.

## Built with

1. [Python 3.8.2](https://www.python.org/doc/)
2. [Flask; Python framework used.](https://flask.palletsprojects.com/en/1.1.x/)
3. [HTML](https://www.w3schools.com/html/)
4. [CSS](https://www.w3schools.com/css/)
5. [MDB 4.8.10](https://mdbootstrap.com/)

## TEAM

[Hassan Juma ](https://github.com/HASSAN1A)

## [License](https://github.com/HASSAN1A/News-App/blob/master/LICENSE.md)

[MIT](https://github.com/HASSAN1A/News-App/blob/master/LICENSE.md) © [Hassan Juma](https://github.com/HASSAN1A)
