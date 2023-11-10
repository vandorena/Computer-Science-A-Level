function Send-OutlookMailFromTemplate
{
    <#
        .SYNOPSIS
        Sends an email from an Outlook Template (oft-file).

        .DESCRIPTION
        Sends an email from an Outlook Template (oft-file) which you composed earlier.
        Optionally, you can specify an Attachment to be added to the email message when sending.
	This allows you to reuse your template but send it with an up-to-date attachment.

        .PARAMETER Path
        Specifies the path to the oft-file.

        .PARAMETER Attachment
        Optional: Specifies the path to the Attachment.

        .EXAMPLE
        PS C:\> Send-OutlookMailFromTemplate -Path "D:\Templates\My Template.oft"

	.NOTES
	Author: Robert Sparnaaij
	Version: 1.0

        .LINK
        Online version: https://www.howto-outlook.com/howto/schedule-recurring-email.htm

    #>

	[CmdletBinding(DefaultParameterSetName='Send')]
	Param
	(
		[Parameter(Mandatory=$true, Position=0, ParameterSetName='Send')]
		[string] $Path,
		[Parameter(Mandatory=$false, Position=1, ParameterSetName='Send')]
		[string] $Attachment
	)

	If (Get-Process Outlook -ErrorAction SilentlyContinue)
	{$OutlookAlreadyRunning = $true} Else {$OutlookAlreadyRunning = $false}

	$olApp = New-Object -ComObject Outlook.Application
	$objMsg = $olApp.CreateItemFromTemplate($Path)

	If ($Attachment) {
		If (Test-Path $Attachment) {
			$objAttachment = $objMsg.Attachments
			$objAttachment.Add($Attachment) | Out-Null
			[System.Runtime.Interopservices.Marshal]::ReleaseComObject($objAttachment) | Out-Null
		}
	}
	$objMsg.Send()
	[System.Runtime.Interopservices.Marshal]::ReleaseComObject($objMsg) | Out-Null

	If ($OutlookAlreadyRunning -eq $false) {
		$olApp.Quit()
		[System.Runtime.Interopservices.Marshal]::ReleaseComObject($olApp) | Out-Null
		Remove-Variable olApp
	}
}
