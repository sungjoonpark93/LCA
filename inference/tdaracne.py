__author__ = 'SungJoonPark'
import rpy2.robjects as robjects
import pandas as pd
from rpy2.robjects import pandas2ri
pandas2ri.activate()


def run_TDARACNE(rootdir,start_point=None,end_point=None):
    #rootdir = "../../data/preprocess/#1/"

    robjects.r('''
    library("Biobase")
    library(TDARACNE)
    getPreprocessedDFAggwihthMean <- function(dirName, starttimepoint ,endtimepoint){

      #dirName = "../../data/preprocess/#1/"
      #endtimepoint = 20
      meanDF <- NULL
      for(fileNum in starttimepoint:endtimepoint){
        fileName <- paste(dirName,paste(toString(fileNum),".csv",sep = ''),sep = "/")
        df <- read.csv(fileName,sep = ',')
        means <- colMeans(df)
        meanDF<-rbind(meanDF,means)
      }
      #meanDF is timepoint x TF expression dataframe
      row.names(meanDF) <- as.character(starttimepoint:endtimepoint)

      return(meanDF)
    }

    getMinimumExpressionSet <- function(DF)
    {
      return(ExpressionSet(as.matrix(t(DF))))

    }

    ''')

    get_agg_with_mean_df = robjects.r['getPreprocessedDFAggwihthMean']
    get_minimum_expression_set = robjects.r['getMinimumExpressionSet']
    TDARACNE = robjects.r['TDARACNE']


    mean_df = get_agg_with_mean_df(rootdir,start_point,end_point)
    min_expression_set = get_minimum_expression_set(mean_df)
    adj = TDARACNE(min_expression_set,11,delta=3,likehood=1.2,norm=2,logarithm=1,thresh=0,ksd=0,tolerance=0.15,plot=False ,dot=False ,adj = True)

    row_names = robjects.conversion.ri2py(robjects.r['rownames'](adj))
    column_names = robjects.conversion.ri2py(robjects.r['colnames'](adj))
    #convert R matrix data struture to python pandas DataFrame

    adj = pd.DataFrame(robjects.pandas2ri.ri2py(adj),index=row_names,columns=column_names)

    return adj


if __name__ =='__main__':
    rootdir = "Q:/LCA/data/preprocess_data/06_23/drug_data_fill_blank_by_lastobservation/#1/"
    adj =  run_TDARACNE(rootdir,start_point=10,end_point=14)
    print adj