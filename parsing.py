import re
import sys

from selenium import webdriver
get_args_from_content = re.compile("def solution[(](.*)[)]")

def get(driver, problem_num):
    driver.get('https://programmers.co.kr/learn/courses/30/lessons/{}'.format(problem_num))
    

def click_python(driver):
    try:
        driver.find_element_by_css_selector("#tour7 > button").click()
        driver.find_element_by_link_text("Python3").click()
    except:
        print("Click Python: Failed |", end = ' ')
        

def get_solution(driver):
    try:
        content = driver.find_element_by_css_selector("#tour3 > div > div").text
        content = '\n'.join(filter(lambda x: not x.strip().isdecimal(), content.split('\n')))
    except:
        print('Get Solution.py: Falied |', end = ' ')
    return content


def get_args(content):
    args = get_args_from_content.match(content).group(1).split(',')
    if args:
        args = list(map(lambda x: x.strip().lower(), args))
    return args


def get_test_case(driver, problem_num, args):
    try:
        theads = driver.find_elements_by_css_selector("#tour2 > div > div > table > thead")
        for idx, thead in enumerate(theads):
            thead = thead.text.split(' ')
            thead = list(map(lambda x: x.lower(), thead))
            if thead[:-1] == args:
                break            
        tbody = driver.find_elements_by_css_selector("#tour2 > div > div > table > tbody")[idx]
        tbody = tbody.find_elements_by_css_selector("tr > td")
    except:
        print("Get thead, tbody: Failed |", end = ' ')
    return thead, tbody


def parsing(problem_num):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('window-size=1920x1080')
    op.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    prefs = {
        "profile.managed_default_content_settings.images": 2,
        "disk-cache-size": 4096
    }
    op.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome('/home/gunmo/public/chromedriver', options=op)
    driver.implicitly_wait(3)
    
    get(driver, problem_num)

    driver.find_element_by_css_selector("#step-0 > div:nth-child(3) > svg").click()

    click_python(driver)
    
    content = get_solution(driver)
    
    args = get_args(content)

    f = open('u_{}.py'.format(problem_num), 'w')
    f.write(content)

    if args == None:
        print('args None')
        f.close()
        return

    thead, tbody = get_test_case(driver, problem_num, args)
    thead_len = len(thead)
    
    if thead[:-1] != args:
        print('thead != args')
        f.close()
        return
        
    f.write('\n\nif __name__ == "__main__":\n    t_case = []\n')
    
    t_case = "    t_case.append([{}]) # return {}\n"

    test_case = []
    for idx, tb in enumerate(tbody):
        if (idx + 1 ) % thead_len == 0:
            f.write(t_case.format(','.join(test_case), tb.text))
            test_case = []
            continue
        test_case.append(tb.text)
    
    f.write('    for tc in t_case:\n        print(solution(*tc))')
    f.close()

if __name__ == "__main__":
    problem_num = sys.argv[1]
    parsing(problem_num)
