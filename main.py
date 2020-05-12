""" Recommended to use insted of multiprocessing_main.py """


if __name__ == "main":

    import finger
    import multiprocessing
    import dbConnector
    import os
    import sys
    import psutil
    import ray

    user_file_path = "" # tells where the user file exists...
    database_location = dbConnector.DATABASE_PARENT_DIR

    if sys.platform in ("linux", "linux2"):
        string_ender = "/"
    else:
        # windows platform
        string_ender = "\\"

    image_matched = False

    # ray.init(num_cpus=psutil.cpu_count()) # leaving a single core

    # @ray.remote
    def check_details(dir_img_name: str):
        """
        if returned True, that means image matched...
        if returned False, meaning that image is not the specific directory image...
        """
        directory = database_location + f"database_fprecog{string_ender}"
        global image_matched
        if not image_matched:
            if finger.match(directory + dir_img_name, user_file_path):
                image_matched = True
                if dbConnector.all_details(dir_img_name) == "are present":
                    dbConnector.print_details(dir_img_name)
                    sys.exit()
                dbConnector.edit_exstng_file(dir_img_name)
                sys.exit()

    def start_execution():

        global image_matched

        dir_elements = list(os.listdir(database_location + f"database_fprecog{string_ender}"))
        dir_elements = tuple(filter(lambda x: x.endswith(".png") or x.endswith(".tif"), dir_elements))

        if dir_elements == ():
            # if there are no elements in the directory...
            random_name = dbConnector.get_name()
            dbConnector.add_txt(random_name) 
            dbConnector.add_fp_img(user_file_path, random_name)
            sys.exit()

        elif len(dir_elements) == 1:
            # if there is a single image....
            # check_details.remote(*dir_elements)

            check_details(*dir_elements)
            # *used asterisk over here to unpack the tuple for a single element.

        else:
            '''
            # using parallel processing if supported for multiple images...

            # ! NOT WORKING PROPERLY
            """
            results = [check_details.remote(img) for img in dir_elements]
            not_ready = True
            while not_ready:
                _, not_ready = ray.wait(results, num_returns=2)
            """
            # !
            '''

            # sequential execution...
            counter, length = 0, len(dir_elements)
            while not image_matched and counter < length:
                image = dir_elements[counter]
                check_details(image)
                counter+=1
            
        # ray.shutdown()

        if not image_matched:
            # if a not single image have matched...
            random_name = dbConnector.get_name()
            dbConnector.add_txt(random_name)
            dbConnector.add_fp_img(user_file_path, random_name)
            sys.exit()

