'''
IT IS NOT RECOMMENDED TO USE THIS FILE.
IT CONTAINS FLAWS
'''


if __name__ == "multiprocess_main":

    import finger
    import multiprocessing
    import dbConnector
    import os
    import sys

    user_file_path = "" # tells where the user file exists...
    database_location = dbConnector.DATABASE_PARENT_DIR

    if sys.platform in ("linux", "linux2"):
        string_ender = "/"
    else:
        string_ender = "\\"

    image_matched = False
    _cpu_cores = multiprocessing.cpu_count()

    if _cpu_cores in (1, 2, ):
        pool = multiprocessing.Pool(_cpu_cores - 1)
        pool_closed = False


    def check_details(dir_img_name: str):
        """
        if returned True, that means image matched...
        if returned False, meaning that image is not the specific directory image...
        """

        directory = database_location + f"database_fprecog{string_ender}"

        def close_pool():
            """
            This will close the pool that is currently executing Globally..
            """
            global pool
            pool.close()
            pool.terminate()
            pool.join()

        global image_matched, pool, pool_closed

        if not image_matched:

            if finger.match(directory + dir_img_name, user_file_path):

                image_matched = True

                if dbConnector.all_details(dir_img_name) == "are present":
                    dbConnector.print_details(dir_img_name)
                    close_pool(); pool_closed = True

                dbConnector.edit_exstng_file(dir_img_name)
                close_pool(); pool_closed = True
        

    def start_execution():

        global image_matched, pool, pool_closed

        list_of_dir_elements = list(os.listdir(database_location + f"database_fprecog{string_ender}"))
        tuple_of_dir_elements = list(filter(lambda x: x.endswith(".png") or x.endswith(".tif"), list_of_dir_elements))
        if tuple_of_dir_elements == ():
            random_name = dbConnector.get_name()
            dbConnector.add_txt(random_name) 
            dbConnector.add_fp_img(user_file_path, random_name)
            sys.exit()

        elif len(tuple_of_dir_elements) == 1:
            check_details(*tuple_of_dir_elements)

        else:
            # if _cpu_cores are 1 or 2, then go for sequential processing...
            # the only way to achieve parallel processing is via multiprocessing.Process class
            # but for image processing it is not suitable...(may break the OS)
            if _cpu_cores in (1, 2, ):
                for image in tuple_of_dir_elements:
                    if image_matched:
                        break
                    check_details(image)

    # >>>>>>>> MAY NOT WORKING PROPERLY <<<<<<<<
    # ============================================================================

            else:    
                # leave at least a single processor core for other executions...
                pool.map(check_details, tuple_of_dir_elements)
                if not pool_closed:
                    pool.close()
                    pool.join()

    # ============================================================================

        if not image_matched:

            random_name = dbConnector.get_name()
            dbConnector.add_txt(random_name)
            dbConnector.add_fp_img(user_file_path, random_name)
            sys.exit()
