import pandas as pd
from selenium import webdriver
import time
from datetime import datetime
from tqdm import tqdm


# webdriver setup
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

# linkedin search urls DS, DA e DE in USA
linkedin_urls = [
    'https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
    'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
    'https://www.linkedin.com/jobs/search?keywords=Data%20Engineer&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    ]

# loop for each url
for counter, url in enumerate(linkedin_urls):
    # goes to url
    driver.get(url)

    # scroll to end of page and waits in order to load more jobs
    SCROLL_PAUSE_TIME = 11

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for k in range(100):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        try:
            # after some scrolls to jobs won't load and a show more button will appear
            # this is a way to click it
            show_more_jobs = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/button')
            show_more_jobs.click()
            time.sleep(SCROLL_PAUSE_TIME)
        except:
            pass


        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # getting all li elements because each one is a job element
    search_results = driver.find_element_by_class_name('jobs-search__results-list')
    jobs = search_results.find_elements_by_tag_name('li')
    print(f"Found {len(jobs)} jobs")

    # getting the url from each element
    jobs_urls = []
    for i in range(len(jobs)):
        try:
            job_url = driver.find_element_by_xpath(f'//*[@id="main-content"]/section[2]/ul/li[{i+1}]/div/a').get_attribute('href')
        except:
            job_url = driver.find_element_by_xpath(f'//*[@id="main-content"]/section[2]/ul/li[{i+1}]/a').get_attribute('href')
        jobs_urls.append(job_url)

    ##### getting the job description
    df_jobs = pd.DataFrame()
    for job_url in tqdm(jobs_urls): # loop for each url
        try:
            driver.get(job_url) # goto url
            # get job name
            job_name = driver.find_element_by_css_selector('#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h1').text
            try:
                # if the job description is too long, a show more button will appear
                # this will click it and wait
                show_more_btn = driver.find_element_by_css_selector('#main-content > section.core-rail > section.description > div.description__text.description__text--rich > section > button.show-more-less-html__button.show-more-less-html__button--more')
                show_more_btn.click()
                time.sleep(0.5)
            except:
                pass
            # getting job description
            job_description = driver.find_element_by_class_name('description').text
            # getting job location (not used)
            job_location = driver.find_element_by_css_selector('#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h4 > div:nth-child(1) > span.topcard__flavor.topcard__flavor--bullet').text
            time.sleep(2)

            # dataframe template: job_name, job_descp, job_location and 0, 1 or 2 encoding the job class
            temp = pd.DataFrame({
                "JobName":[job_name],
                "JobDescription":[job_description],
                "JobLocation":[job_location],
                "Label":[counter]
            })
            df_jobs = df_jobs.append(temp, ignore_index=True)
            df_jobs.to_excel("jobs.xlsx") # save for each iteration

        except Exception as e:
            print(e) # if there's a problem with some job, it'll move on to the next one