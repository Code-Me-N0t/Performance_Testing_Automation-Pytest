from src.modules import *
from src.gameapp import get_gameurl

url = get_gameurl()

@pytest.mark.firstload
def test_FIRSTLOAD(driver):
    loads = []

    for i in range(100):
        driver.get(url)
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#layaContainer'))
        )
        start_time = time.time()

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#layaContainer > audio'))
            )
        except: continue

        end_time = time.time()
        load_time = end_time - start_time
        print(f'Load Time {i}: {Fore.GREEN}{round(load_time, 2)} seconds')
        loads.append(round(load_time, 2))
    
    avg_load_time = sum(loads) / len(loads) if loads else 0
    print(f'First Load Average Load Time: {Fore.BLUE}{round(avg_load_time, 2)}')
    
    desktop_firstload = {
        'load_times': loads,
        'average_load_time': round(avg_load_time, 2)
    }

    with open('desktop_firstload.json', 'w') as json_file:
        json.dump(desktop_firstload, json_file, indent=4)

@pytest.mark.cached
def test_CACHED(driver):
    loads = []
    
    for i in range(100):
        driver.get(url)

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#layaContainer'))
        )
        start_time = time.time()

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#layaContainer > audio'))
            )
        except: continue

        end_time = time.time()
        load_time = end_time - start_time
        print(f'Load Time {i}: {Fore.GREEN}{round(load_time, 2)} seconds')
        loads.append(round(load_time, 2))
    
    avg_load_time = sum(loads) / len(loads) if loads else 0
    print(f'Cached Average Load Time: {Fore.BLUE}{round(avg_load_time, 2)}')
    
    desktop_cached = {
        'load_times': loads,
        'average_load_time': round(avg_load_time, 2)
    }

    with open('desktop_cached.json', 'w') as json_file:
        json.dump(desktop_cached, json_file, indent=4)

def get_js_heap_size(driver):
    result = driver.execute_cdp_cmd('Performance.getMetrics', {})
    metrics = {metric['name']: metric['value'] for metric in result['metrics']}
    js_heap_size = metrics['JSHeapUsedSize'] / (1024 * 1024)
    return js_heap_size


@pytest.mark.memory
def test_MEMORY(driver):
    ini_heap_sizes = []
    peak_heap_sizes = []

    for i in range(100):
        driver.get(url)
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#layaContainer'))
        )

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#layaContainer > audio'))
            )
        except: continue

        initial_js_heap_size = get_js_heap_size(driver)
        print(f'\n[{i}]Initial JS Heap Size: {Fore.GREEN}{initial_js_heap_size:.2f} MB')
        ini_heap_sizes.append(round(initial_js_heap_size, 2))

        sleep(5)
        pyautogui.click(330, 450)
        sleep(10)

        peak_js_heap_size = get_js_heap_size(driver)
        print(f'[{i}]Peak JS Heap Size: {Fore.GREEN}{peak_js_heap_size:.2f} MB')
        peak_heap_sizes.append(round(peak_js_heap_size, 2))
            
    avg_ini_heap_size = sum(ini_heap_sizes) / len(ini_heap_sizes) if ini_heap_sizes else 0
    avg_peak_heap_size = sum(peak_heap_sizes) / len(peak_heap_sizes) if peak_heap_sizes else 0

    print(f'Average Initial JS Heap Size: {Fore.BLUE}{avg_ini_heap_size:.2f} MB')
    print(f'Average Peak JS Heap Size: {Fore.BLUE}{avg_peak_heap_size:.2f} MB')

    memory_stats = {
        'Initial JS Heap Sizes':       ini_heap_sizes,
        'Average Initial Heap Size':   round(avg_ini_heap_size, 2),
        'Peak JS Heap Sizes':          peak_heap_sizes,
        'Average Peak Heap Size':      round(avg_peak_heap_size, 2)
    }

    with open('memory_stats.json', 'w') as json_file:
        json.dump(memory_stats, json_file, indent=4)


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

@pytest.mark.cpu
def test_CPU(driver):
    initial_usage = []
    highest_usage = []

    for i in range(100):
        driver.get(url)
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})

        cpu = []

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#layaContainer'))
        )

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#layaContainer > audio'))
            )
        except: continue

        cpu_usage = get_cpu_usage()
        print(f'\n[{i}]Initial CPU Usage: {Fore.GREEN}{cpu_usage}%')
        cpu.append(cpu_usage)
        initial_usage.append(cpu_usage)

        sleep(5)
        pyautogui.click(330, 450)
        sleep(2)
        for _ in range(10):
            cpu_usage = get_cpu_usage()
            cpu.append(cpu_usage)
            sleep(1)
        
        highest_cpu_usage = max(cpu)
        highest_usage.append(highest_cpu_usage)

        print(f'[{i}]Highest CPU Usage: {Fore.GREEN}{highest_cpu_usage}%')
    
    avg_icpu_usage = sum(initial_usage)/len(initial_usage)
    avg_hcpu_usage = sum(highest_usage)/len(highest_usage)

    print(f'Average Initial CPU Usage: {Fore.BLUE}{round(avg_icpu_usage, 2)}%')
    print(f'Average Highest CPU Usage: {Fore.BLUE}{round(avg_hcpu_usage, 2)}%')

    cpu_stats = {
        'Initial CPU Usage': initial_usage,
        'Average Initial CPU Usage': round(avg_icpu_usage, 2),
        'Highest CPU Usage': highest_usage,
        'Average Highest CPU Usage': avg_hcpu_usage
    }

    with open('cpu_stats.json', 'w') as json_file:
        json.dump(cpu_stats, json_file, indent=4)