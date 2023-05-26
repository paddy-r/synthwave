from typing import Final, Annotated, List, Dict

USOC_FIELDS: Final[Annotated[List[str], 56]] = [
    'hidp', 'pidp', 'ppid', 'fnspid', 'mnspid', 'gor_dv', 'indinus_xw',
    'hhdenus_xw', 'pns1pid', 'pns2pid', 'depchl_dv', 'mastat_dv', 'jbstat',
    'hiqual_dv', 'maedqf', 'paedqf', 'fimnpen_dv', 'fimnmisc_dv',
    'fiyrinvinc_dv', 'ficode', 'istrtdaty', 'hsownd', 'sex_dv', 'age_dv',
    'scghqa', 'scghqb', 'scghqc', 'scghqd', 'scghqe', 'scghqf', 'scghqg',
    'scghqh', 'scghqi', 'scghqj', 'scghqk', 'scghql', 'fimnsben_dv', 'paygu_dv',
    'seearngrs_dv', 'j2pay_dv', 'sf1', 'sf2a', 'sf2b', 'sf3a', 'sf3b', 'sf4a',
    'sf4b', 'sf5', 'sf6a', 'sf6b', 'sf6c', 'sf7', 'scflag_dv', 'jbft_dv',
    'sclfsato', 'finnow']

USOC_NAME_MAP: Final[Annotated[Dict[str, str], 56]] = {
    'hidp': 'id_household',
    'pidp': 'id_person',
    'ppid': 'id_partner',
    'fnspid': 'id_father',
    'mnspid': 'id_mother',
    'pns1pid': 'id_parent1',
    'pns2pid': 'id_parent2',
    'gor_dv': 'location',
    'indinus_xw': 'weight_person',
    'hhdenus_xw': 'weight_household',
    'depchl_dv': 'indicator_dependent_child',
    'mastat_dv': 'label_marital_status',
    'jbstat': 'label_job_status',
    'hiqual_dv': 'label_highest_qualification',
    'maedqf': 'label_mother_education',
    'paedqf': 'label_father_education',
    'fimnpen_dv': 'income_pension',
    'fimnmisc_dv': 'income_miscellaneous',
    'fiyrinvinc_dv': 'income_investment',
    'fimnsben_dv': 'income_benefits',
    'paygu_dv': 'income_pay',
    'seearngrs_dv': 'income_self_employment',
    'j2pay_dv': 'income_second_job',
    'ficode': 'label_income',
    'istrtdaty': 'year',
    'hsownd': 'label_house_ownership',
    'sex_dv': 'sex',
    'age_dv': 'age',
    'scghqa': 'label_ghq_a',
    'scghqb': 'label_ghq_b',
    'scghqc': 'label_ghq_c',
    'scghqd': 'label_ghq_d',
    'scghqe': 'label_ghq_e',
    'scghqf': 'label_ghq_f',
    'scghqg': 'label_ghq_g',
    'scghqh': 'label_ghq_h',
    'scghqi': 'label_ghq_i',
    'scghqj': 'label_ghq_j',
    'scghqk': 'label_ghq_k',
    'scghql': 'label_ghq_l',
    'sf1': 'label_general_health',
    'sf2a': 'label_health_limits_a',
    'sf2b': 'label_health_limits_b',
    'sf3a': 'label_health_limits_c',
    'sf3b': 'label_health_limits_d',
    'sf4a': 'label_emotions_a',
    'sf4b': 'label_emotions_b',
    'sf5': 'label_pain',
    'sf6a': 'label_feel_calm',
    'sf6b': 'label_have_energy',
    'sf6c': 'label_feel_depressed',
    'sf7': 'label_social_activities_interference',
    'scflag_dv': 'indicator_self_completion',
    'jbft_dv': 'indicator_full_part_time',
    'sclfsato': 'label_life_satisfaction',
    'finnow': 'label_financial_situation'}

USOC_FIELDS_SPLIT: Final[Annotated[Dict[str, List[str]], 6]] = {
    'indall': ['hidp', 'pidp', 'ppid', 'fnspid', 'mnspid', 'gor_dv', 'pns1pid',
               'pns2pid', 'depchl_dv', 'mastat_dv', 'sex_dv', 'scflag_dv'],
    'indresp': ['hidp', 'pidp', 'ppid', 'fnspid', 'mnspid', 'indinus_xw',
                'pns1pid', 'pns2pid', 'depchl_dv', 'mastat_dv', 'jbstat',
                'hiqual_dv', 'maedqf', 'paedqf', 'fimnpen_dv', 'fimnmisc_dv',
                'fiyrinvinc_dv', 'istrtdaty', 'sex_dv', 'scghqa', 'scghqb',
                'scghqc', 'scghqd', 'scghqe', 'scghqf', 'scghqg', 'scghqh',
                'scghqi', 'scghqj', 'scghqk', 'scghql', 'fimnsben_dv',
                'paygu_dv', 'seearngrs_dv', 'j2pay_dv', 'sf1', 'sf2a', 'sf2b',
                'sf3a', 'sf3b', 'sf4a', 'sf4b', 'sf5', 'sf6a', 'sf6b', 'sf6c',
                'sf7', 'scflag_dv', 'jbft_dv', 'sclfsato', 'finnow'],
    'hhresp': ['hidp', 'hhdenus_xw', 'hsownd'],
    'youth': ['hidp', 'pidp', 'fnspid', 'mnspid', 'pns1pid', 'pns2pid',
              'sex_dv'],
    'child': ['hidp', 'pidp', 'fnspid', 'mnspid', 'pns1pid', 'pns2pid',
              'depchl_dv', 'sex_dv'],
    'income': ['hidp', 'pidp', 'ficode']}

FICODE: Final[Annotated[Dict[str, int], 36]] = {
    'ni_retirement_state_retirement_old_age_pension': 1,
    'a_pension_from_a_previous_employer': 2,
    'a_pension_from_a_spouses_previous_employer': 3,
    'a_private_pension_annuity': 4,
    'a_widows_or_war_widows_pension': 5,
    'a_widowed_mothers_allowance_widowed_parents_allowance_bereavement'
    '_allowance': 6,
    'pension_credit_includes_guarantee_credit_and_saving_credit': 7,
    'severe_disablement_allowance': 8,
    'industrial_injury_disablement_allowance': 9,
    'disability_living_allowance': 10,
    'attendance_allowance': 11,
    'carers_allowance_formerly_invalid_care_allowance': 12,
    'war_disablement_pension': 13,
    'incapacity_benefit': 14,
    'income_support': 15,
    'job_seekers_allowance': 16,
    'national_insurance_credits': 17,
    'child_benefit_including_lone_parent_child_benefit_payments': 18,
    'child_tax_credit': 19,
    'working_tax_credit_includes_disabled_persons_tax_credit': 20,
    'maternity_allowance': 21,
    'housing_benefit': 22,
    'council_tax_benefit': 23,
    'educational_grant_not_student_loan_or_tuition_fee_loan': 24,
    'trade_union_friendly_society_payment': 25,
    'maintenance_or_alimony': 26,
    'payments_from_a_family_member_not_living_here': 27,
    'rent_from_boarders_or_lodgers_not_family_members_living_here_with_you': 28,
    'rent_from_any_other_property': 29,
    'foster_allowance_guardian_allowance': 30,
    'rent_rebate': 31,
    'rate_rebate': 32,
    'employment_and_support_allowance': 33,
    'return_to_work_credit': 34,
    'sickness_and_accident_insurance': 35,
    'in_work_credit_for_lone_parents': 36}
