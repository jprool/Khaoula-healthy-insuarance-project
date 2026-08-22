
# Claims data-quality contract

CLAIMS_WARN_RULES = {
    "known_patient_gender":
        "patient_gender IN ('MALE', 'FEMALE', 'OTHER')",

    "service_type_present":
        "service_type IS NOT NULL",

    "provider_specialty_present":
        "provider_specialty IS NOT NULL"
}


CLAIMS_DROP_RULES = {
    "claim_id_present":
        "claim_id IS NOT NULL",

    "patient_id_present":
        "patient_id IS NOT NULL",

    "policy_number_present":
        "policy_number IS NOT NULL",

    "patient_age_valid":
        "patient_age BETWEEN 0 AND 120"
}


CLAIMS_FAIL_RULES = {
    "claim_amount_non_negative":
        "claim_amount >= 0",

    "service_not_after_claim":
        "service_date <= claim_date"
}


# === PATIENT QUALITY RULES START ===

PATIENT_WARN_RULES = {
    "birth_date_present":
        "birth_date IS NOT NULL",

    "medical_record_number_present":
        "medical_record_number IS NOT NULL",

    "given_name_present":
        "given_name IS NOT NULL",

    "family_name_present":
        "family_name IS NOT NULL",

    "recognized_gender":
        "gender IN ('MALE', 'FEMALE', 'OTHER', 'UNKNOWN')",

    "phone_present":
        "phone IS NOT NULL"
}


PATIENT_DROP_RULES = {
    "patient_id_present":
        "patient_id IS NOT NULL",

    "age_logically_valid":
        "age IS NULL OR age BETWEEN 0 AND 120",

    "birth_date_not_future":
        "birth_date IS NULL OR birth_date <= current_date()"
}


PATIENT_FAIL_RULES = {}

# === PATIENT QUALITY RULES END ===


# === CONDITION QUALITY RULES START ===

CONDITION_WARN_RULES = {
    "encounter_reference_present":
        "encounter_id IS NOT NULL",

    "condition_name_present":
        "condition_name IS NOT NULL",

    "recognized_clinical_status":
        "clinical_status IN ('ACTIVE', 'RESOLVED')",

    "recognized_verification_status":
        "verification_status IN ('CONFIRMED')",

    "onset_datetime_present":
        "onset_datetime IS NOT NULL"
}


CONDITION_DROP_RULES = {
    "condition_id_present":
        "condition_id IS NOT NULL",

    "patient_id_present":
        "patient_id IS NOT NULL",

    "condition_code_present":
        "condition_code IS NOT NULL"
}


CONDITION_FAIL_RULES = {
    "condition_timeline_valid":
        """
        onset_datetime IS NULL
        OR abatement_datetime IS NULL
        OR abatement_datetime >= onset_datetime
        """
}

# === CONDITION QUALITY RULES END ===


# === ENCOUNTER QUALITY RULES START ===

ENCOUNTER_WARN_RULES = {
    "practitioner_reference_present":
        "practitioner_id IS NOT NULL",

    "organization_reference_present":
        "organization_id IS NOT NULL",

    "encounter_type_present":
        "encounter_type IS NOT NULL",

    "recognized_status":
        "status IN ('FINISHED')",

    "recognized_encounter_class":
        "encounter_class IN ('AMB', 'EMER', 'IMP')",

    "start_datetime_present":
        "start_datetime IS NOT NULL"
}


ENCOUNTER_DROP_RULES = {
    "encounter_id_present":
        "encounter_id IS NOT NULL",

    "patient_id_present":
        "patient_id IS NOT NULL"
}


ENCOUNTER_FAIL_RULES = {
    "encounter_timeline_valid":
        """
        start_datetime IS NULL
        OR end_datetime IS NULL
        OR end_datetime >= start_datetime
        """
}

# === ENCOUNTER QUALITY RULES END ===
