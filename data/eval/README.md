# Evaluation Metrics
The manual evaluation files align the Source Text (TP) and Target Text (TA), assessing the MT outputs across three specific columns. Scoring is binary (1 = Correct/Present, 0 = Error/Missing):

Sintagma nominale (_noun phrase_)(1/0) [Micro-level]: Evaluates the correct gender inflection of the noun phrase containing the target female sports nomen agentis.

Accordo (_agreement_) (1/0/N/A) [Macro-level]: Assesses the internal sentence consistency (gender agreement between the target noun phrase and its related modifiers). Marked as N/A (Not Applicable) when the target syntax does not require explicit gender agreement.

Altri errori di traduzione (_other translation errors_) (1/0) [Noise tracking]: Flags the presence of general translation errors unrelated to gender, ensuring the analysis effectively isolates the MT systems' performance on the target phenomenon.

