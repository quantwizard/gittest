from ConfigParser import SafeConfigParser

def main():
    parser = SafeConfigParser()
    parser.add_section('Log')
    parser.set('Log', 'Path', 'config/parser.log')
    parser.set('Log', 'Size', '200')

    # write to config file
    with open('config.cfg', 'r+') as f:
        parser.write(f)
        parser.read(f)
        print parser.get('Log', 'Path')
        print parser.get('Log', 'Size')


if __name__ == '__main__':
    main()