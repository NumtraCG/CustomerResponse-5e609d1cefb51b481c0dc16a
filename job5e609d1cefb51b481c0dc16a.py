import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e609d1cefb51b481c0dc16b','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	CustomerResponse_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e609d1cefb51b481c0dc16b", spark, "{'url': '/Demo/CustomerChurnTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e609d1cefb51b481c0dc16b','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e609d1cefb51b481c0dc16b','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e609d1cefb51b481c0dc16c','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	CustomerResponse_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e609d1cefb51b481c0dc16b"],{"5e609d1cefb51b481c0dc16b": CustomerResponse_DBFS}, "5e609d1cefb51b481c0dc16c", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "customerID"}, "feature": "customerID", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "0002-ORFBO", "max": "9993-LHIEB", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "gender"}, "feature": "gender", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "Female", "max": "Male", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "SeniorCitizen", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2138", "mean": "0.17", "stddev": "0.38", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {"feature_label": "Partner"}, "feature": "Partner", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Dependents"}, "feature": "Dependents", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "tenure", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2138", "mean": "31.76", "stddev": "24.52", "min": "0", "max": "72", "missing": "0"}}, {"transformationsData": {"feature_label": "PhoneService"}, "feature": "PhoneService", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "MultipleLines"}, "feature": "MultipleLines", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "InternetService"}, "feature": "InternetService", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "DSL", "max": "No", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "OnlineSecurity"}, "feature": "OnlineSecurity", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "OnlineBackup"}, "feature": "OnlineBackup", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "DeviceProtection"}, "feature": "DeviceProtection", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "TechSupport"}, "feature": "TechSupport", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "StreamingTV"}, "feature": "StreamingTV", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "StreamingMovies"}, "feature": "StreamingMovies", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Contract"}, "feature": "Contract", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "Month-to-month", "max": "Two year", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "PaperlessBilling"}, "feature": "PaperlessBilling", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "PaymentMethod"}, "feature": "PaymentMethod", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "Bank transfer (automatic)", "max": "Mailed check", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "MonthlyCharges", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2138", "mean": "63.25", "stddev": "30.13", "min": "18.7", "max": "117.6", "missing": "0"}, "transformation": ""}, {"transformationsData": {"feature_label": "TotalCharges"}, "feature": "TotalCharges", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "2203.3", "stddev": "2233.6", "min": " ", "max": "999.45", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Churn"}, "feature": "Churn", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2138", "mean": "", "stddev": "", "min": "No", "max": "Yes", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "customerID_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2138", "mean": "1068.5", "stddev": "617.33", "min": "0.0", "max": "2137.0", "missing": "0"}}, {"feature": "gender_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.48", "stddev": "0.5", "min": "0", "max": "1", "missing": "0"}}, {"feature": "Partner_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.48", "stddev": "0.5", "min": "0", "max": "1", "missing": "0"}}, {"feature": "Dependents_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.29", "stddev": "0.45", "min": "0", "max": "1", "missing": "0"}}, {"feature": "PhoneService_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.1", "stddev": "0.3", "min": "0", "max": "1", "missing": "0"}}, {"feature": "MultipleLines_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.59", "stddev": "0.66", "min": "0", "max": "2", "missing": "0"}}, {"feature": "InternetService_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.81", "stddev": "0.78", "min": "0", "max": "2", "missing": "0"}}, {"feature": "OnlineSecurity_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.72", "stddev": "0.81", "min": "0", "max": "2", "missing": "0"}}, {"feature": "OnlineBackup_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.8", "stddev": "0.79", "min": "0", "max": "2", "missing": "0"}}, {"feature": "DeviceProtection_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.78", "stddev": "0.8", "min": "0", "max": "2", "missing": "0"}}, {"feature": "TechSupport_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.74", "stddev": "0.81", "min": "0", "max": "2", "missing": "0"}}, {"feature": "StreamingTV_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.83", "stddev": "0.77", "min": "0", "max": "2", "missing": "0"}}, {"feature": "StreamingMovies_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.84", "stddev": "0.77", "min": "0", "max": "2", "missing": "0"}}, {"feature": "Contract_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.64", "stddev": "0.8", "min": "0", "max": "2", "missing": "0"}}, {"feature": "PaperlessBilling_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.41", "stddev": "0.49", "min": "0", "max": "1", "missing": "0"}}, {"feature": "PaymentMethod_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "1.31", "stddev": "1.15", "min": "0", "max": "3", "missing": "0"}}, {"feature": "TotalCharges_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2138", "mean": "997.46", "stddev": "614.12", "min": "0.0", "max": "2064.0", "missing": "0"}}, {"feature": "Churn_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2138", "mean": "0.26", "stddev": "0.44", "min": "0", "max": "1", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e609d1cefb51b481c0dc16c','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e609d1cefb51b481c0dc16c','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e609d1cefb51b481c0dc16d','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	CustomerResponse_AutoML = tpot_execution.Tpot_execution.run(["5e609d1cefb51b481c0dc16c"],{"5e609d1cefb51b481c0dc16c": CustomerResponse_AutoFE}, "5e609d1cefb51b481c0dc16d", spark,json.dumps( {"model_type": "classification", "label": "Churn", "features": ["customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"], "percentage": "30", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "", "ProjectName": "OrphenTest", "PipelineName": "CustomerResponse", "pipelineId": "5e609d1cefb51b481c0dc16a", "userid": "5e39734e0204cd465d4d2e10", "runid": "", "url_ResultView": "http://40.83.140.93:3200", "experiment_id": "551308251382540"}))

	PipelineNotification.PipelineNotification().completed_notification('5e609d1cefb51b481c0dc16d','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e609d1cefb51b481c0dc16d','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)

