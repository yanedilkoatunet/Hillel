# CSS Locators

```css
a.header_logo
a.header_logo[routerlink="/"]
a.header-link.-active
button[appscrollto="aboutSection"]
button[appscrollto="contactsSection"]
button.btn.header-link
button.header-link.-guest
button.header_signin
button.btn-outline-white.header_signin
button.hero-descriptor_btn.btn-primary
a.socials_link[href*="facebook.com"]
a.socials_link[href*="t.me"]
a.socials_link[href*="youtube.com"]
a.socials_link[href*="instagram.com"]
a.socials_link[href*="linkedin.com"]
a.contacts_link[href="https://ithillel.ua"]
a.contacts_link[href^="mailto:"]
button.close[aria-label="Close"]
input#signupName
input#signupLastName[name="lastName"]
input#signupEmail.form-control
input[type="password"][name="password"]
input#signupRepeatPassword
button.btn-primary[disabled]
input#signupPassword + input#signupRepeatPassword
```
# XPath Locators

```xpath
//a[@routerlink='/' and contains(@class, 'header_logo')]
//a[@routerlink='/' and normalize-space(text())='Home']
//button[@appscrollto='aboutSection']
//button[@appscrollto='contactsSection']
//button[contains(@class, 'header-link') and normalize-space(text())='About']
//button[contains(@class, 'header-link') and normalize-space(text())='Contacts']
//button[contains(@class, '-guest') and normalize-space(text())='Guest log in']
//button[contains(@class, 'header_signin') and normalize-space(text())='Sign In']
//button[contains(@class, 'hero-descriptor_btn') and normalize-space(text())='Sign up']
//a[@href='https://www.facebook.com/Hillel.IT.School' and @target='_blank']
//a[contains(@href, 't.me/ithillel_kyiv') and contains(@class, 'socials_link')]
//a[contains(@href, 'youtube.com') and @rel='nofollow']
//a[contains(@href, 'instagram.com') and contains(@class, 'socials_link')]
//a[contains(@href, 'linkedin.com/school/ithillel') and @target='_blank']
//a[@href='https://ithillel.ua' and contains(@class, 'contacts_link')]
//a[contains(@href, 'mailto:developer@ithillel.ua') and contains(@class, 'contacts_link')]
//button[@type='button' and @aria-label='Close']
//input[@id='signupName' and @name='name']
//input[@id='signupLastName' and @formcontrolname='lastName']
//input[@id='signupEmail' and @type='text' and @name='email']
//input[@name='email' and @formcontrolname='email' and contains(@class, 'form-control')]
//input[@id='signupPassword' and @type='password']
//input[@name='repeatPassword' and @formcontrolname='repeatPassword']
//button[@type='button' and normalize-space(text())='Register']
//input[@id='signupPassword']/following-sibling::*[1][self::input and @id='signupRepeatPassword']
```
