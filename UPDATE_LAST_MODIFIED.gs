// Responds to a change in `input` Range by setting current timestamp in the cell calling this function
function UPDATE_LAST_MODIFIED(input) {
  // general docs
  // https://developers.google.com/apps-script/reference/spreadsheet
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  // https://developers.google.com/apps-script/reference/utilities/utilities#formatDate(Date,String,String)
  var time = Utilities.formatDate(new Date(), "GMT", "yyyy-MM-dd'T'HH:mm'Z'");
  return time;
}
