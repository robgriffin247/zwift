setwd('~/github/personal/zwift/')

library(googlesheets4)
library(readr)

sheet_names <- c('dropshop', 'test_log', 'r_out_segment_results')
for(sheet_name in sheet_names){
  write_csv(
    read_sheet('https://docs.google.com/spreadsheets/d/1OTQfpj_nz-QSHyUl-2iwW0y2on74BK8YKJDUF03iAyk/', sheet=sheet_name),
    paste0('data/', sheet_name, '.csv'))
}