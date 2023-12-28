import subprocess

def run_file():
    print('=====> Starting the process...')
    process = subprocess.Popen(['./CONG_42021'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print('Process finished.')
    print('Output:', out)
    if err:
        print('Error:', err)

run_file()