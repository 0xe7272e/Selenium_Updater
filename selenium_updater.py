"""Class for updating selenium scripts. - 0xe7272e"""
import argparse

class SeleniumUpdater:
    """Class for updating script"""
    def __init__(self , old_file_path, new_file_path):
        self.old_file_path = old_file_path
        self.new_file_path = new_file_path
        # It's necesary to check if the file was previusly opened
        try:
            with open(self.old_file_path, 'r') as fp:
                self.code = fp.read()
                self.old_code = self.code
        except:
            print(f"{self.old_file_path} was unable to be opened")
            exit()

    def update_single_selectors(self):
        """
        Update selectors of single elements in the source code of the
        file.
        """
        self.code = self.code.replace('find_element_by_xpath(' , 'find_element("xpath",')
        self.code = self.code.replace('find_element_by_css_selector(' , 'find_element("css_selector",')
        self.code = self.code.replace('find_element_by_link_text(' , 'find_element("link_text",')
        self.code = self.code.replace('find_element_by_class_name(' , 'find_element("class_name",')
        self.code = self.code.replace('find_element_by_partial_link_text(' , 'find_element("partial_link_text",')
        self.code = self.code.replace('find_element_by_name(' , 'find_element("name",')
        self.code = self.code.replace('find_element_by_id(' , 'find_element("id",')
        
    def update_general_selectors(self):
        """
        Update selectors of single elements in the source code of the
        file.
        """
        self.code = self.code.replace('find_elements_by_xpath(' , 'find_elements("xpath",')
        self.code = self.code.replace('find_elements_by_css_selector(' , 'find_elements("css_selector",')
        self.code = self.code.replace('find_elements_by_link_text(' , 'find_elements("link_text",')
        self.code = self.code.replace('find_elements_by_class_name(' , 'find_elements("class_name",')
        self.code = self.code.replace('find_elements_by_partial_link_text(' , 'find_elements("partial_link_text",')
        self.code = self.code.replace('find_elements_by_name(' , 'find_elements("name",')
        self.code = self.code.replace('find_elements_by_id(' , 'find_elements("id",')
        
    def update_script(self):
        """Update the script into the new file path"""
        self.update_single_selectors()
        self.update_general_selectors()
        print(f'old code : \n {self.old_code} \n\n\n new code:\n {self.code}' )
        with open(f"{self.new_file_path}" , 'w') as fp:
            fp.write(self.code)
        print(f'new file {self.new_file_path} generated!')

if __name__ == "__main__":
    """Main Script"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f' , '--old_file' , required=True, help="path of the non-updated script")
    parser.add_argument('-o' , '--output' , required=True, help="path of the output file")
    args = parser.parse_args()
    updater = SeleniumUpdater(args.old_file, args.output)
    updater.update_script()
