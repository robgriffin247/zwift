setwd('~/github/personal/zwift/')

library(data.table)
#library(httr)
library(rvest)
library(googlesheets4)

source_files <- list.files('data/strava_sourcefiles/')

segment_results <- rbindlist(lapply(source_files, function(source_file){
  source_data <- read_html(paste0('data/strava_sourcefiles/', source_file))

  source_text <- as.character(html_nodes(source_data, 'body'))
  
  segments <- tstrsplit(tstrsplit(tstrsplit(source_text, 'preload segment efforts')[[2]], 
                                  'pageView.activity')[[1]], 'start_index')
  
  segments[[1]] <- NULL
  
  data.table(t(sapply(segments, function(segment){
    segment_name <- unlist(tstrsplit(tstrsplit(segment, '\"name\\\":\"')[2], '\"')[1])
    #segment_watts <- unlist(tstrsplit(tstrsplit(segment, '\"avg_watts\\\":\"')[2], '\\\\')[1])
    segment_time <- as.numeric(tstrsplit(tstrsplit(segment, '\"elapsed_time_raw\":')[2], ',')[1])
    list(gsub('view-source_https___www.strava.com_activities_|.html','',source_file) ,
         segment_name, segment_time)
    })))[V2!="NULL"]
}))

setnames(segment_results, c('test_id', 'segment_name', 'time'))

write_sheet(segment_results, ss='https://docs.google.com/spreadsheets/d/1OTQfpj_nz-QSHyUl-2iwW0y2on74BK8YKJDUF03iAyk/', sheet='segment_results_R')
