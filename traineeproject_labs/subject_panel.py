from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import swab
from .processing_profiles import sars_pcr_processing

subject_lab_profile = LabProfile(
    name='traineeproject_lab_profile',
    requisition_model='traineeproject_subject.subjectrequisition'
)

sars_pcr_panel = RequisitionPanel(
    name='sars_cov2_pcr',
    verbose_name='SARS-COV-2 PCR',
    aliquot_type=swab,
    processing_profile=sars_pcr_processing)

subject_lab_profile.add_panel(sars_pcr_panel)    
site_labs.register(subject_lab_profile)