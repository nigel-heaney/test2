#!/usr/bin/env python

import logging


class logit():
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

    def loginfo(self, output):
        """This
        """
        logging.info(output)

    def logwarn(self, output):
        """This
        """
        logging.warning(output)

    def logcritical(self, output):
        """This"""
        logging.critical(output)

    def logerror(self, output):
        """This
        """
        logging.error(output)

    def logdebug(self, output):
        """This
        """
        logging.debug(output)


def main():
    x = logit()
    x.logfilename = "./test.log"
    x.startlog()
    x.logwarn("test")
    x.logcritical("test")
    x.loginfo("test")
    x.logdebug("test")


if __name__ == '__main__':
    main()
