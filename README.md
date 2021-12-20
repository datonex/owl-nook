# <img src="static/img/logo/owl-only/owl-coral.png" height="50" /> Owl Nook

## Overview

### What is this website for?

The blog if for the user to find all kinds of information in one convenient place as well as share tips and funny things to the general internet.

### What does it do?

Reddit type blog full of all kinds of posts. This includes news, tips and posts just for laughs from memes to your next book to your next cocktail party type drinks. Users can posts or just browse what other people have posted. Unregistered users have very little access to content nad must join to view the entire post.

### How does it work

The website is going to be blog type layout. For those users who are there just to browse can expand on the post they are interested in but they will need to have an account to view the content. They can also save posts to read later. For those who love to share content they also need to have an account and can create posts and add photos at their own convenience. The website is built using the Django framework to handle creating user accounts and managing the website. The Postgres database is used to store general user data so that they can access their information later.

:point_right: [Live Website](https://owl-nook.herokuapp.com/) :desktop_computer:

:point_right: [GitHub Repository](https://github.com/datonex/owl-nook)

## UX & UI design

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

### User Stories

| **Role**     | **Summary**                              | **Feature**                                   |
| ------------ | ---------------------------------------- | --------------------------------------------- |
| ADMIN        | approve comments                         | filter out objectionable comments             |
| USER         | register an account                      | comment, like and view full content           |
| USER         | leave comments on a post                 | be involved in the conversion                 |
| USER         | upvote and downvote posts                | interact with content                         |
| USER         | save posts                               | access content easily at my own convenience   |
| USER         | open posts                               | read full text                                |
| USER         | view the date/time of an individual post | see which content is most up to date/ or not. |
| USER         | add categories to post                   | can get to the topics I want                  |
| USER         | filter post                              | control what content i see first              |
| USER         | follow a user                            | easily see their posts                        |
| USER / ADMIN | view the number of likes on each post    | see which is the most popular or viral        |
| USER / ADMIN | create posts                             | post blog content                             |
| USER / ADMIN | view comments on an individual posts     | read the conversation                         |
| USER / ADMIN | create draft posts                       | finish writing the content later              |

The Agile tool of choice to plan and manage my work is [Trello](https://trello.com/). The workflow is illustrated [here](https://trello.com/b/EE8FIF7B) :point_left:

### Design

#### Wireframes

Wireframes were created using [Balsamiq Wireframes](https://balsamiq.com/). The website design was inspired by the the [Medium](https://medium.com/), [Reddit](https://www.reddit.com/) and [Philosophy](https://preview.colorlib.com/#philosophy) template

The website design was based on a mobile first design and based on the features from the user stories. The website logo is to be fixed at the top right of the page and the bottom left of the footer. All register/login buttons will be in the header, fixed at the top right corner of the device.

##### :iphone: Mobile Wireframes

Click here for mobile [pdf versions](README/wireframes/mobile.pdf) :point_left:

- _Homepage_

  The homepage is meant to be simple and allows the user to view incoming posts straight away wether they are a new user or a returning user. New posts are displayed large and clearly on at the top of the page. The featured image of the blog will be large and the title with other details displayed over it. Older posts are show underneath in smaller cards with the featured image on the left content and titles on the right. The page will infinitely scroll until the first post.

  <img src="README/wireframes/img/mobile/homepage.png" height="300" />

- _Blog post_

  The blog post page will have a centered title and the user will be able to see the author of the post easily. There will be a featured image represented by the blank image and the content below it. Registered users will be able to rate and post on comments

  <img src="README/wireframes/img/mobile/blog-post.png" height="300" />

- _Category_

  Each blog post will have a category or topic that is assigned by the author of the post (category is displayed by the button under the content on blog post) When the user clicks on the button they are redirected to the category page where they will be able to view all posts in that category. Again the page will infinitely scroll.

  <img src="README/wireframes/img/mobile/category.png" height="300" />

- _About us_

  Pages that include information about Owl Nook, the legal pages and privacy pages will be based on this template.

  <img src="README/wireframes/img/mobile/about-us.png" height="300" />

- Forms: _Contact Us, Sign up, Login_

  All the forms wil be based on these templates using the appropriate for each. Ideally they will fill the entire screen and there should be no need to scroll vertically or horizontally.

  <img src="README/wireframes/img/mobile/sign-up_sign-in.png" height="300" /> <img src="README/wireframes/img/mobile/contact-us.png" height="300" />

##### :iphone: Tablet Wireframes

Click here for tablet [pdf versions](README/wireframes/tablet.pdf) :point_left:

The tablet wireframes are very similar to the mobile wireframes with minor modifications the content and elements to fit the screen size.

<img src="README/wireframes/img/tablet/homepage.png" height="350" /> <img src="README/wireframes/img/tablet/blog-post.png" height="350" /> <img src="README/wireframes/img/tablet/category.png" height="350" /> <img src="README/wireframes/img/tablet/about-us.png" height="350" /> <img src="README/wireframes/img/tablet/sign-up_sign-in.png" height="350" /> <img src="README/wireframes/img/tablet/contact-us.png" height="350" />

##### :desktop_computer: Desktop Wireframes

Click here for Desktop [pdf versions](README/wireframes/desktop.pdf) :point_left:

The desktop wireframes are very similar to the tablet wireframes with minor modifications the content and elements to fit the screen size. The footer will be constantly displayed as the user scrolls including the categories on the right side of the page.

<img src="README/wireframes/img/desktop/homepage.png" height="300" /> <img src="README/wireframes/img/desktop/blog-post.png" height="300" /> <img src="README/wireframes/img/desktop/category.png" height="300" /> <img src="README/wireframes/img/desktop/about-us.png" height="300" /> <img src="README/wireframes/img/desktop/sign-up_sign-in.png" height="300" /> <img src="README/wireframes/img/desktop/contact-us.png" height="300" />

#### Colour Scheme

The colour scheme was generated randomly using the [coolors](https://coolors.co/ffffff-b0b7bf-0e103d-f87575) generator. I wanted it to be a dark mode theme. Initially the generator started with 5 colours but they were too many. I reduced it to three (navy, coral and grey). When I began creating the mockups, the grey did not have enough contrast with the background, particularly with small text. As a result I added white to the colour palette.

![colour palette](README/mockups/components/colour-palette.png)

The components and mockups were made using [Figma](https://www.figma.com/). The components were generated from [Creatt Studios](https://www.figma.com/@creatt) wireframe kit. When I began creating the mockups the colour scheme was more or less the same. some elements like the accent colours were quite distracting. For example the horizontal rule under the blog title. I decreased the transparency so that to help breakup text and sections but without distracting the user from reading the content. the image below will show the same colours used originally by with varying degrees of transparency reducing by 20% each time.

[![colour palette](README/mockups/components/img/colors.png)](README/mockups/components/pdf/colors.pdf)

Click here for [pdf version](README/mockups/components/pdf/colors.pdf) :point_left:

#### Typography

The font used for headings and content text is Poppins, with a backup font of sans serif. The nature of the website means that there are sections where there will be a lot of text. Poppins is a font that looks good in large and small text and, the user can also easily distinguish letters. Depending on what the user posts, wether it be italic text for quotes, or title, The entire Poppins family of fonts and font weights will be available to the user.

[![typography](README/mockups/components/img/typography.png)](README/mockups/components/pdf/typography.pdf)

Click here for [pdf version](README/mockups/components/pdf/typography.pdf) :point_left:

#### Imagery

Blog images will be posted by a user. The user must post an image when posting a blog, otherwise a default image will be used. The default image is a woman sitting typing on a laptop on a ceramic desk.

#### Buttons and button groups

Buttons and any other button groups will be based on this template below. to ensure consistent formatting when the scope of the project increases.

[![buttons](README/mockups/components/img/buttons.png)](README/mockups/components/pdf/buttons.pdf)

Click here for [pdf version](README/mockups/components/pdf/buttons.pdf) :point_left:

#### Content Blocks

Content blocks will be derived from the following template even when the scope of the project increases.

[<img src="README/mockups/components/img/content-blocks.png" height="500">](README/mockups/components/pdf/content-blocks.pdf)

Click here for [pdf version](README/mockups/components/pdf/content-blocks.pdf) :point_left:

#### Form elements

Form elements for the blog will be based in template below, This includes text input, textarea and checkboxes

[![buttons](README/mockups/components/img/form-elements.png)](README/mockups/components/pdf/form-elements.pdf)

Click here for [pdf version](README/mockups/components/pdf/form-elements.pdf) :point_left:

#### Other elements and reference components

The following items were used for reference to aid creation of components for Owl Nook website.

- [Helper Blocks](README/mockups/components/pdf/helpers.pdf) :point_left:

- [Navigation](README/mockups/components/pdf/navigation-components-dark.pdf) :point_left:

- [Shadows and other shenanigans](README/mockups/components/pdf/shadow-and-other-shenanigans.pdf) :point_left:

#### Mockups

Links will open on the Figma website and no login is required.

[Mobile wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=2%3A3) :point_left:

[Tablet wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=2%3A2) :point_left:

[Desktop wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=0%3A1) :point_left:

#### Interactive prototype

The prototypes for tablet and mobile are not shown as they are identical to the desktop prototype. To interact with the prototype, click the play button on the top right corner of the screen as shown below :point_down:

![play prototype button](README/prototype-interaction.png)

This will allow you to view the flow of the website and some of the interactions with the buttons.

[Desktop prototype](https://www.figma.com/file/DpvgBd6vfV7ZxK9vpB97pc/?node-id=0%3A1) :point_left:

### Database

#### Conceptual ERD

The database for this project began a conceptual ERD to show the relationship between each entity. Each user entity that is created either be an admin or regular member. If the user is an administrator, they have permission to add, edit or delete the category names. The normal user will only have permission to read the category and assign it to a blog post.

Each user can create a blog post entity, a comment and a reading list to save a blog post to read at their convenience.

[![conceptual ERD](README/DBMS/img/revised-conceptual-ERD.png)](README/DBMS/pdf/revised-conceptual-ERD.pdf)

Click here for [pdf version](README/DBMS/pdf/revised-conceptual-ERD.pdf) 👈

#### Physical ERD model

The physical ERD model will illustrate how the entities and their information will be added to the database. I will be using crow foot notation to demonstrate the relationships.

- Each user entity has a **User_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Author**.

- **User_ID** attribute will also be used be used as the foreign key **Member** attribute in the Comment entity.

- Each category has a **Category_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Category**.

- Each blog post has a **Blog_Post_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Category**.

- **Blog_Post_ID** attribute will also be used be used as the foreign key **Blog_post** attribute in the reading list entity.

[![physical ERD](README/DBMS/img/revised-ERD-crows-foot.png)](README/DBMS/pdf/revised-ERD-crows-foot.pdf)

Click here for [pdf version](README/DBMS/pdf/revised-ERD-crows-foot.pdf) 👈

### Existing Features

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

#### Common Features Across All Pages

- [x] **Header** - allows user to easily navigate across all pages

- Header is fixed to top of page for easy access (desktop and large tablets)
- Zimbabwe logo and text are positioned on the left and are links that take you to the homepage
- Navigation is place on the right on the logo for easy access (under logo for mobile)
- Navigation links change colour when hovered over. This lets the visitor know that it is clickable.
- Navigation link is underlined to let user know what page they are on
- Entire header disappears for mobile devices
- Colors have been chosen with optimum contrast in mind to be pleasant to the eye.
- [x] **Links** that are hovered over
- All links that are surrounding text have been underlined and change color when hovered over. This helps the user to identify external links. (except logo)
- [x] **Navigation banner**
- Navigation banner is the same across all pages to give uniformity and familiarity
- background image on home is scrollable to give a more fun user experience
- [x] **Accessibility**
- All images have aria labels in case they don't load and for the visually impaired
- [x] **Buttons**
- All buttons have the same styling and they invert colours when hovered (except for scroll to top button)
- [x] **Responsiveness**
- All pages work well with many screen sizes
- [x] **Footer**
- Footer sticks to the bottom of the page, regardless of the amount of content. This aids the overall user experience.
- All content have near uniform layout to give a nice and engaging flow of text and images
- Social links have been grouped together
- 'Contact us' is form for feedback and any question the user might have

### Specific to Pages

- [x] **Home Page**

- Image grid to easily see a handful of places the user can visit. When the mouse hovers you get addition information about the location

### Features Left to Implement

- Add a page where you can make a booking for a particular destinations. this includes adding a virtual online basket so that users can see what they have already selected (requires **Javascript** knowledge) For this reason I decided to remove the booking page from the website because it would be too incomplete and not provide a positive user experience.

- hide the scroll to top button at the beginning of page

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### Languages used

- [HTML](https://en.wikipedia.org/wiki/HTML5) - Add content and formatting to web page.
- [CSS](https://en.wikipedia.org/wiki/CSS) - Add styling and colours to web page.
- [JavaScript](https://www.javascript.com/) - Add interactive features to web page

- [Python](https://www.python.org/) - Add code to allow app to access database.

### Frameworks, Libraries and Programs Used

- [Visual Studio Code](https://code.visualstudio.com/) - Source-code editor optimised for debugging, testing, syntax highlighting and extension support

- [Git](https://git-scm.com/) - used to allow for tracking of any changes in the code and for the version control.

- [Github](https://github.com/) - used to host the project files

- [Heroku](https://www.heroku.com/) - used to deploy web application

- [Postgres](https://postgresapp.com/) - used as the DBMS to store user profile data and hosted on Heroku

- [Balsamiq Wireframes](https://balsamiq.com/) - used to create wireframes

- [Figma](https://www.figma.com/) - used to create mockups and prototypes

- [Creatt Studios](https://www.figma.com/@creatt) - component template to illustrate mockups

- [Google Sheets](https://docs.google.com/spreadsheets/) - Tabulate user stories

- [Zapier](https://www.zapier.com/) - Automate process of adding user stories from google sheets to Trello

- [Trello](https://trello.com/) - Agile tool of choice to manage and plan web app.

- [MindNode](https://www.mindnode.com/) - app used to draw mind maps to show entities and their attributes.

- [Lucid Chart](https://www.lucidchart.com/) - web app use to illustrated database schema.

- [Canva](https://www.canva.com/) - webapp used to design logo and favicon.

- [Django](https://www.djangoproject.com/) - Python web framework to create web application and provide security to users.

- [Fontawesome](https://fontawesome.com/) - to insert icons in the website to make site more visually appealing and easy to navigate.

- [Favicon.io](https://favicon.io/) - used to generate favicon to webpage

- [Google Fonts](https://fonts.google.com/) - used to import 'Poppins' fonts in the style.css stylesheet.

- [TinyPNG](https://tinypng.com/) - used to reduce resolution of images

- [Bootstrap](https://getbootstrap.com/) - Used for the responsive layout as well as custom components such as image carousel, navigation bar, footer, cards, and collapse element.

- [jquery](https://jquery.com/) - Used in some of the clickable elements such as collapsible 'hamburger' nav bar and collapse element.

- [popper.js](https://popper.js.org/) - Used in some of the clickable elements such as collapsible 'hamburger' navbar and collapse element.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:

- Go to the "Contact Us" page
- Try to submit the empty form and verify that an error message about the required fields appears
- Try to submit the form with an invalid email address and verify that a relevant error message appears
- Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

- ### Navigation bar

- When the logo or 'Zimbabwe' text is clicked, the user is redirected to the home page
- All links are working and have been tested.
- navigation bar is aligned vertically and under the logo for screens smaller than 660px
- The navigation bar stays at the top of the page for screens larger than 660px only

- ### Footer

- Footer always sticks to the bottom of the page and was tested by removing all content from the page.
- social media link open in a new tab when clicked
- When user accesses the 'Contact us' page

  - Name is required to continue submission
  - Email field is required and has to be in the correct format.
  - Text field has to contain at least two characters.
  - terms and conditions have to be ticked
  - When 'Submit' is clicked (given all fields have been filled out) the form will be sent

- ### The Image grid

- Any image that is hovered on (desktop only) the text is uniformly aligned and shows correct information for another device the grid is hidden and a continuous prose is displayed instead.

- ### External links

- All social links in the footer bring the user to the relevant social pages
- Links to external websites, the booking and visa button bring the user to the right website in a new tab.

- ### Internal Links

- Logo and text all lead to home page
- Navigation links lead to relevant pages
- Contact us link leads to the correct page for all web pages

### CSS3 validator

Pass

<a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border: 0; width: 88px; height: 31px;" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!" /></a>

### HTML5 Validator

**Home Page** - Pass
**About Page** - Pass
**Contact Us** - Pass
**Travel Information Page** - 2 Errors

1. Error: The element a must not appear as a descendant of the button element

   From line 345, column 63; to line 345, column 118

   `="button"><a href="https://www.evisa.gov.zw/home" target="_blank">Apply`

   <!-- markdownlint-disable-next-line MD029 -->

2. Error: The element a must not appear as a descendant of the button element.

From line 376, column 38; to line 376, column 89

`="button"><a href="https://www.expedia.co.uk" target="_blank">Book f`

### Compatibility Testing

- Browser Compatibility

| Screen size\Browser |       Safari       |    Opera    | Microsoft Edge |       Chrome       |      Firefox       | Internet Explorer |
| ------------------- | :----------------: | :---------: | :------------: | :----------------: | :----------------: | :---------------: |
| Mobile              | :heavy_check_mark: | Not Tested  |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Desktop             | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Tablet              | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |

- OS Compatibility was tested on iOS 14.5.1, MacOS Catalina, iPadOS 14.5 It is yet to be tested on Unix, Linux, Windows or Solaris Operating Systems.
- The devices used in this testing include MacBook Pro, iPad Pro, iPhone 12 Pro Max, iPhone 7 Plus.

- The website was exhaustively tested for responsiveness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). Different viewport sizes were simulated ranging from as small as iPhone 5 (320px) to large desktop sizes (1200px and above).

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

This website was published using [GitHub Pages](https://pages.github.com/).

1. Go to the GitHub.com and log in.
2. On the left-hand side, you'll see all your repositories, select the appropriate one.
3. Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.
4. Scroll down till you see 'Pages' heading.
5. Under the 'Source' click on the dropdown and select 'master branch'
6. The page will reload and you'll see the link of your published page displayed under 'GitHub' pages.
7. It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.

### Contribution

1. Firstly you will need to clone this repository by running the `git clone <https://github.com/datonex/visit-zimbabwe/>` command
2. If using VS Code type make sure you have th Git extension installed then type about code into your terminal
3. Download the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension, one installed find the go live button at the bottom right of your vscode window
4. The project will now run on [localhost](http://127.0.0.1:5500/)
5. If using Gitpod use the command `python3 -m http.server`
6. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Content

Each bit of content must have its own link and displayed as a list

- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media

Each bit of content must have its own link and displayed as a list

#### Images

- video was obtained from [here](https://linkhere.com)

#### Audio

- audio was obtained from [here](https://linkhere.com)

#### Video

- video was obtained from [here](https://linkhere.com)

### Acknowledgements

I received inspiration for this project from following tourists sites

- Thank you to my mentor for his support and guidance
