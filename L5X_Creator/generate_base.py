"""Generates the base L5X file"""

def generate_base(project_name,
                  fw_version,
                  backplane,
                  owner,
                  processor_type,
                  processor_major,
                  processor_minor,
                  project_path):
    """docstring"""
    datetime = "test"
    filename = project_path+project_name+".L5X"
    file = open(filename, "w+")
    file.write(f"""
               <?xmlversion="1.0" encoding="UTF-8" standalone="yes"?>\n
               <RSLogix5000Content SchemaRevision="1.0" SoftwareRevision="{fw_version}" TargetName="{project_name}" TargetType="Controller" ContainsContext="false" Owner="{owner}" ExportDate="{datetime}" ExportOptions="DeocratedData ForceProtectedEncoding AllProjDocTrans">
               <Controller Use="Target" Name="{project_name}" ProcessorType="{processor_type}" MajorRev="{processor_major}" MinorRev="{processor_minor}" TimeSlice="20" ShareUnusedTimeSlice="1" ProjectCreationDate="{datetime}" LastModifiedDate="{datetime}" SFCExecutionControl="CurrentActive" SFCRestartPostition="MostRecent"
               SFCLastScan="DontScan" ProjectSN="16#0000_0000" MatchProjectToController="false" CanUseRPIFromProducer="false" InhibitAutomaticFirmwareUpdate="0" PassThroughConfiguration="EnabledWithAppend" DownloadProjectDocumentationAndExtendedProperties="true">
               <RedundancyInfo Enabled="false" KeepTestEditsOnSwitchOver="false" IOMemoryPadPercentage="90" DataTablePadPercentage="50"/>
               <Security Code="0" ChangesToDetect="16#ffff_ffff_ffff_ffff"/>
               <SafetyInfo/>
               <DataTypes/>
               <Modules>
               <Module Name="Local" CatalogNumber="{processor_type}" Vendor="1" ProductType="14" ProductCode="92" Major="{processor_major}" Minor="{processor_minor}" ParentModule="Local" ParentModPortID="1" Inhibited="false" MajorFault="true"
               >
               EKey State="ExactMatch"/>
               <Ports>
               <Port Id="1" Address="0" Type="ICP" Upstream="false">
               <Bus Size="{backplane}"/>
               </Port>
               </Ports>
               </Module>
               </Modules>
               <AddOnInstructionDefinitions/>
               <Tags/>
               <Programs>
               <Program Name="MainProgram" TestEdits="false" MainRoutineName="MainRoutine" Disabled="false" UseAsFolder="false">
               <Tags/>
               <Routines>
               <Routine Name="MainRoutine" Type="RLL"/>
               </Routines>
               </Program>
               </Programs>
               <Tasks>
               <Task Name="MainTask" Type="CONTINUOUS" Priority="10" Watchdog="500" DisableUpdateOutputs="false" InhibitTask="false">
               <ScheduledPrograms>
               <ScheduledProgram Name="MainProgram"/>
               </ScheduledPrograms>
               </Task>
               </Tasks>
               <CST MasterID="0"/>
               <WallClockTime LocalTimeAdjustment="0" TimeZone="0"/>
               <Trends/>
               <DataLogs/>
               <TimeSynchronize Priority1="128" Priority2="128" PTPEnable="false"/>
               </Controller>
               </RSLogix5000Content>
                """)
    file.close()
