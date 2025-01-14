CREATE DATABASE SampleDatabase;
USE DATABASE SampleDatabase;
CREATE SCHEMA LOGGING_AND_TRACING;
USE SCHEMA LOGGING_AND_TRACING;
CREATE EVENT TABLE SAMPLEDATABASE.LOGGING_AND_TRACING.SAMPLE_EVENTS;;
ALTER ACCOUNT SET EVENT_TABLE = SAMPLEDATABASE.LOGGING_AND_TRACING.SAMPLE_EVENTS;
ALTER DATABASE STREAMLIT_TEST SET LOG_LEVEL = INFO;
ALTER DATABASE SAMPLEDATABASE SET TRACE_LEVEL = ON_EVENT;