$(document).ready( function() {     
      
      $("#id_ProjectID").hide();
      $('label[for="id_ProjectID"]').hide();

      $("#id_Location").hide();
      $('label[for="id_Location"]').hide();

      $("#id_ProjectName").hide();
      $('label[for="id_ProjectName"]').hide();

      $("#id_NoOfBH").hide();
      $('label[for="id_NoOfBH"]').hide();

      $("#id_DepthOfBH").hide();
      $('label[for="id_DepthOfBH"]').hide();

      $("#id_Drilling_Method").hide();
      $('label[for="id_Drilling_Method"]').hide();

      $("#id_ReportingOfficer").hide();
      $('label[for="id_ReportingOfficer"]').hide();

      $("#id_SubmittedTo").hide();
      $('label[for="id_SubmittedTo"]').hide();

      $("#id_GroundWaterTableDepth").hide();
      $('label[for="id_GroundWaterTableDepth"]').hide();

      $('select[id="id_InvoiceTypes"]').hide();
      $('label[for="id_InvoiceTypes"]').hide();

      $("#id_InvAmount").hide();
      $('label[for="id_InvAmount"]').hide();

      $("#id_QuotAmount").hide();
      $('label[for="id_QuotAmount"]').hide();

      $("#id_QuotClientName").hide();
      $('label[for="id_QuotClientName"]').hide();


  $('input[id="id_typ_0"]').click(function(){
    $('select[id="id_InvoiceTypes"]').show();
    $('label[for="id_InvoiceTypes"]').show();

    $("#id_InvAmount").show();
    $('label[for="id_InvAmount"]').show();

    $("#id_ProjectID").hide();
    $('label[for="id_ProjectID"]').hide();

    $("#id_Location").hide();
    $('label[for="id_Location"]').hide();

    $("#id_ProjectName").hide();
    $('label[for="id_ProjectName"]').hide();

    $("#id_NoOfBH").hide();
    $('label[for="id_NoOfBH"]').hide();

    $("#id_DepthOfBH").hide();
    $('label[for="id_DepthOfBH"]').hide();

    $("#id_Drilling_Method").hide();
    $('label[for="id_Drilling_Method"]').hide();

    $("#id_ReportingOfficer").hide();
    $('label[for="id_ReportingOfficer"]').hide();

    $("#id_SubmittedTo").hide();
    $('label[for="id_SubmittedTo"]').hide();

    $("#id_GroundWaterTableDepth").hide();
    $('label[for="id_GroundWaterTableDepth"]').hide();

    $("#id_QuotAmount").hide();
    $('label[for="id_QuotAmount"]').hide();

    $("#id_QuotClientName").hide();
    $('label[for="id_QuotClientName"]').hide();
  });
  $('input[id="id_typ_1"]').click(function(){
    $("#id_QuotAmount").show();
    $('label[for="id_QuotAmount"]').show();

    $("#id_QuotClientName").show();
    $('label[for="id_QuotClientName"]').show();

    $("#id_ProjectID").hide();
    $('label[for="id_ProjectID"]').hide();

    $("#id_Location").hide();
    $('label[for="id_Location"]').hide();

    $("#id_ProjectName").hide();
    $('label[for="id_ProjectName"]').hide();

    $("#id_NoOfBH").hide();
    $('label[for="id_NoOfBH"]').hide();

    $("#id_DepthOfBH").hide();
    $('label[for="id_DepthOfBH"]').hide();

    $("#id_Drilling_Method").hide();
    $('label[for="id_Drilling_Method"]').hide();

    $("#id_ReportingOfficer").hide();
    $('label[for="id_ReportingOfficer"]').hide();

    $("#id_SubmittedTo").hide();
    $('label[for="id_SubmittedTo"]').hide();

    $("#id_GroundWaterTableDepth").hide();
    $('label[for="id_GroundWaterTableDepth"]').hide();

    $('select[id="id_InvoiceTypes"]').hide();
    $('label[for="id_InvoiceTypes"]').hide();

    $("#id_InvAmount").hide();
    $('label[for="id_InvAmount"]').hide();
  });
  $('input[id="id_typ_2"]').click(function(){

      $("#id_ProjectID").show();
      $('label[for="id_ProjectID"]').show();

      $("#id_Location").show();
      $('label[for="id_Location"]').show();

      $("#id_ProjectName").show();
      $('label[for="id_ProjectName"]').show();

      $("#id_NoOfBH").show();
      $('label[for="id_NoOfBH"]').show();

      $("#id_DepthOfBH").show();
      $('label[for="id_DepthOfBH"]').show();

      $("#id_Drilling_Method").show();
      $('label[for="id_Drilling_Method"]').show();

      $("#id_ReportingOfficer").show();
      $('label[for="id_ReportingOfficer"]').show();

      $("#id_SubmittedTo").show();
      $('label[for="id_SubmittedTo"]').show();

      $("#id_GroundWaterTableDepth").show();
      $('label[for="id_GroundWaterTableDepth"]').show();

      $('select[id="id_InvoiceTypes"]').hide();
      $('label[for="id_InvoiceTypes"]').hide();

      $("#id_InvAmount").hide();
      $('label[for="id_InvAmount"]').hide();

      $("#id_QuotAmount").hide();
      $('label[for="id_QuotAmount"]').hide();

      $("#id_QuotClientName").hide();
      $('label[for="id_QuotClientName"]').hide();
  });
});