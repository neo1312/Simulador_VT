import java.lang.Exception
from datetime import datetime


# DBLogger utilities #

DB_TABLE_NAME = 'EVENT_LOGS'
PROJECT_NAME = system.project.getProjectName()


class Logger:
	
    def __init__(self, name):
    	
    	self.name = name
    	self.logger = system.util.getLogger(self.name)
    
    def to_db(self, level, message):
    	
    	log_method = getattr(self.logger, level.lower(), None)
    	
    	if log_method:
    		log_method(message)
    		
    		params = {
    			'table_name': DB_TABLE_NAME,
    			'logger': self.name, 
    			'message': message, 
    			'level_': level.upper(),
    			'project': PROJECT_NAME, 
    			'time_stamp': datetime.now()
    			}
    		try:
    			system.db.runNamedQuery(PROJECT_NAME, "DBLogger/Insert", params)
    		except java.lang.Exception as e:
				self.logger.error("%s" % e)
	else:
			self.logger.error("Level is not valid")