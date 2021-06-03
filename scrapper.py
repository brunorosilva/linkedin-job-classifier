import pandas as pd
from selenium import webdriver
import time
import urllib.request
from datetime import datetime
from tqdm import tqdm


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

# ds br url = 'https://www.linkedin.com/jobs/search/?geoId=106057199&keywords=data%20scientist&location=Brazil&sortBy=R&redirect=false&position=1&pageNum=0'
# ds usa url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
# de usa url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Engineer&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0' # de usa
url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
driver.get(url)

SCROLL_PAUSE_TIME = 11

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

for k in range(100):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    try:
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


search_results = driver.find_element_by_class_name('jobs-search__results-list')
jobs = search_results.find_elements_by_tag_name('li')
print(f"Found {len(jobs)} jobs")

jobs_urls = []
for i in range(len(jobs)):
    try:
        job_url = driver.find_element_by_xpath(f'//*[@id="main-content"]/section[2]/ul/li[{i+1}]/div/a').get_attribute('href')
    except:
        job_url = driver.find_element_by_xpath(f'//*[@id="main-content"]/section[2]/ul/li[{i+1}]/a').get_attribute('href')
    jobs_urls.append(job_url)

pd.DataFrame({"JOBURL":jobs_urls}).to_csv('jobs_urls_data_analyst.csv')

df_jobs = pd.DataFrame()
for job_url in tqdm(jobs_urls):
    try:
        driver.get(job_url)
        job_name = driver.find_element_by_css_selector('#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h1').text
        try:
            show_more_btn = driver.find_element_by_css_selector('#main-content > section.core-rail > section.description > div.description__text.description__text--rich > section > button.show-more-less-html__button.show-more-less-html__button--more')
            show_more_btn.click()
            time.sleep(0.5)
        except:
            pass
        job_description = driver.find_element_by_class_name('description').text
        job_location = driver.find_element_by_css_selector('#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h4 > div:nth-child(1) > span.topcard__flavor.topcard__flavor--bullet').text
        time.sleep(2)
        temp = pd.DataFrame({
            "JobName":[job_name],
            "JobDescription":[job_description],
            "JobLocation":[job_location]
        })
        df_jobs = df_jobs.append(temp, ignore_index=True)
        df_jobs.to_excel("jobs_usa_data_analyst.xlsx")

    except Exception as e:
        print(e)




# job_company = job.find_element_by_xpath('div/h4').text
#         job_location = job.find_element_by_xpath('div/div/span[1]').text
#         try:
#             job_ez_apply_exists = job.find_element_by_xpath('div/div/span[2]')
#             job_ez_apply = True
#         except:
#             job_ez_apply = False
#         job.click()
#         time.sleep(3)
#         try:
#             job_img = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[1]/div[1]/a/img')
#             job_img_src = job_img.get_attribute('src')
#             show_more = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/div/section/button[1]').click()
#             time.sleep(1)
#             job_description = driver.find_element_by_xpath('//*[@id="main-content"]/section/div[2]/section[2]/div/section/div').text
#             job_meta = driver.find_elements_by_class_name('job-criteria__item')
#             job_seniority = job_meta[0].text
#             job_contract = job_meta[1].text
#             job_function = job_meta[2].text
#             job_industry = job_meta[3].text

#             temp = pd.DataFrame({
#                 "name"              : [job_name],
#                 "company_logo"      : [job_img_src],
#                 "company_name"      : [job_company],
#                 "job_location"      : [job_location],
#                 "is_easy_apply"     : [job_ez_apply],
#                 "job_description"   : [job_description],
#                 "job_seniority"     : [job_seniority],
#                 "employment_type"   : [job_contract],
#                 "job_function"      : [job_function],
#                 "company_industry"  : [job_industry]
#             }, index=[0])
#             df_jobs = df_jobs.append(temp, ignore_index=True)
#             print("{:2%} das vaga concluídas, total de {} vagas".format(i/len(jobs), len(jobs)))
#         except:
#             print("Erro")
#     except Exception as e:
#         print(e)
# df_jobs.to_excel("jobs_{}.xlsx".format(datetime.now()))