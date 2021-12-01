from datetime import datetime

class AppLogger:

    def logger(self,file_obj,messages):
        """
        This function will handle all the error inside project
        :param file_obj: it will take file object where error will be written.
        :param messages: Error message to write
        :return:
        """
        try:
            date=datetime.date()
            time=datetime.now()
            current_time=time.strftime('%H:%M:%S')
            file_obj.write(str(date)+"\t"+str(current_time)+"\t\t"+messages+"\n")

        except OSError as s:
            raise s

        except Exception as e:
            raise e
class Log:

    def __init__(self,name):
        self.name=name
    def log(self):
        logger=lg.ger=lg.getLogger(self.name)
        logger.setLevel(lg.DEBUG)
        format=lg.Formatter("%(asctime)s:%(name)s:(levelname)s:%(message)s")
        filehandler=lg.FileHandler("test.log")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        return logger
