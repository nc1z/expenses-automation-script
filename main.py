from automation import Automation
from build_json import CategoryDataset


def main():
    categoryDataset = CategoryDataset()
    categoryDataset.json_build()
    automation = Automation()
    automation.start_copy_script()
    automation.start_paste_script()


if __name__ == '__main__':
    main()
