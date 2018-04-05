#!/usr/bin/env python
"""
This
"""
import logging


class Logit(object):
    """ this
    """
    def __init__(self):
        """
        This
        """
        self.logfilename = "/var/log/output.log"
        self.dateformat = "%Y-%m-%d_%H-%M-%S"
        self.default_log_level = logging.DEBUG
        self.filemode = 'w'  # a,w

    def startlog(self):
        """This
        """
        logging.basicConfig(filename=self.logfilename, level=self.default_log_level, datefmt=self.dateformat,
                            format='%(asctime)s:%(levelname)8s: %(message)s', filemode=self.filemode)
        logging.info("Logging started")

    @staticmethod
    def loginfo(output):
        """This
        """
        logging.info(output)

    @staticmethod
    def logwarn(output):
        """This
        """
        logging.warning(output)

    @staticmethod
    def logcritical(output):
        """This"""
        logging.critical(output)

    @staticmethod
    def logerror(output):
        """This
        """
        logging.error(output)

    @staticmethod
    def logdebug(output):
        """This
        """
        logging.debug(output)


def main():
    """This
    """
    logger = Logit()
    logger.logfilename = "./test.log"
    logger.startlog()
    logger.logwarn("test")
    logger.logcritical("test")
    logger.loginfo("test")
    logger.logdebug("test")


if __name__ == '__main__':
    main()
