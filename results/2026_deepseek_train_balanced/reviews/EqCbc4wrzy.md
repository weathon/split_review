## Summary

MDPE is a new multimodal deception detection dataset comprising video, audio, and text from 193 subjects (over 104 hours), along with each subject's Big Five personality traits and independently collected emotional expression videos. Its scale (193 subjects vs. 70 in the next largest public dataset) and inclusion of paired individual-difference measurements are genuine contributions. The paper documents a careful data collection protocol with blind interviewer design, monetary incentives, and IRB approval, and provides benchmark experiments using standard feature extractors.

---

## Strengths

1. **Substantially larger than existing public deception datasets** — 193 subjects and 6,209 total minutes (1,808 minutes of deceptive video) versus the next largest (DDPM) at 70 subjects and 776 minutes (Table 1). This is a concrete scaling improvement that addresses the acknowledged limitation of small-sample prior datasets.

2. **Only public deception dataset with paired personality and emotional characteristics for each subject** — The paper collects Big Five questionnaire data (Section 3.3) and a separate 16-video emotional induction experiment for every subject, alongside their deceptive behavior. This enables research on individual differences that no prior dataset supports.

3. **Empirical evidence that personality features improve deception detection in the benchmark** — Across nearly all feature extractors in Tables 2 and 3, adding personality features consistently raises both accuracy and AUC (e.g., Baichuan-13B text: 61.87%/0.649 → 63.74%/0.683; VIT+WMB+Bai multimodal: 63.42%/0.666 → 64.87%/0.681). The trend is consistent and supports the paper's central claim about the value of individual-difference information.

4. **Well-designed data collection protocol** — The interviewer is blinded to which 9 of 24 questions are deceptive; two-tier monetary incentives (150%–200% base pay) incentivize successful deception; warm-up questions establish baseline truthful demeanor; subjects are encouraged to mix truth into lies for naturalistic behavior. These methodological choices (Section 3.3) are documented and replicable.

---

## Weaknesses

### Fatal
None.

### Major

1. **Answer-level (item-level) train/validation split creates potential data leakage** — The paper states: "We randomly select 5 answers (3 truths and 2 deceptions) from 24 answers in all samples as the validation set, and the remaining 19 answers as the training set" (lines 174–175). This is a per-subject split where the same subject contributes responses to both training and validation. A model can learn person-specific visual appearance, voice characteristics, and behavioral patterns from training answers and apply them to validation answers from the same person, meaning the reported numbers may partially reflect person identification rather than deception detection. **There is no subject-level evaluation (e.g., train on 80% of subjects, test on 20%)**, which is the standard setup for testing generalization to unseen individuals — the core practical question for any deception detection system. This undermines the informativeness of the benchmark results as a guide for future work.

2. **No baselines reported** — The dataset has 15 truthful and 9 deceptive responses per subject (62.5% truthful); the validation split has exactly 3 truthful and 2 deceptive per subject, meaning a trivial "always predict truthful" classifier would achieve 60% accuracy. The paper's best unimodal accuracy is 61.87% (Baichuan-13B) and best multimodal is 64.87% — modest gains over a no-information baseline. Yet the paper reports neither a majority-class baseline, a random baseline, nor a simple feature baseline (e.g., logistic regression on eGeMAPS or bag-of-words). Without these, the reader cannot assess whether the models' performance reflects meaningful deception signals or merely weak statistical patterns that may vanish under proper evaluation.

### Minor

1. **Emotional feature extraction pipeline is underspecified** — The paper states: "For emotional features, we train an emotion recognition model first, input all emotional expression samples into the emotion recognition model, and take the last fully connected layer features for average pooling as the emotion expression feature" (line 145). No details are given on the architecture, training data, emotion categories, or accuracy of this model. Since the emotional expression videos and deception videos come from the same subjects, there is a risk the extracted features encode subject identity rather than emotion-specific information. The paper itself notes that emotional features sometimes *hurt* performance (lines 184, 189), which could reflect this issue.

### Trivial
None.

---

## Nice-to-Haves
- The interviewer provides deception judgments and fills out a trust scale (line 98); reporting the interviewer's accuracy as a **human baseline** would be informative and is standard in deception dataset papers.
- **Cross-dataset evaluation** (training on MDPE and testing on another public deception dataset, or vice versa) would strengthen the claim of utility but is beyond the paper's stated scope.
- Clarifying Table 1 by separately reporting deceptive-only duration alongside total duration would improve transparency.

---

## Removed Points
- **Criticism that the textual modality claim is not well-supported** — Table 2 shows text AUCs (0.639–0.649) consistently above audio (0.563–0.636) and visual (0.574–0.602). The claim that text reveals more deceptive clues is supported by the data. Removed as factually incorrect criticism.
- **Criticism that Table 1 is misleading** — The critic speculates that other datasets report only deceptive duration while MDPE reports total duration. The paper does not specify the composition of other datasets' durations. This is speculative. Removed.
- **Criticism about no cross-dataset evaluation** — Standard for a new dataset paper to focus on its own dataset. Nice-to-have but not a weakness. Moved to Nice-to-Have.
- **Criticism about no discussion of data split in limitations section** — This is part of the same issue as the major weakness above; the substance is already covered. Not a separate weakness.

---

## Novel Insights

The most interesting observation that emerges from these reviews is the tension between the paper's strengths and weaknesses: the dataset itself appears to be well-constructed, carefully documented, and genuinely novel in its inclusion of individual-difference measures — yet the evaluation section, which is supposed to demonstrate the dataset's utility, is designed in a way that prevents reliable interpretation of the results. This means the paper's *primary contribution* (the dataset) is solid, while its *secondary contribution* (the benchmark and evidence that personality/emotion features help) is significantly weakened by a methodological choice (answer-level split) that is easily fixable. This asymmetry is unusual — typically in dataset papers, the benchmarks are straightforward and the data collection is the hard part. Here, the data collection is the strong point and the benchmark design is the weak point.

---

## Suggestions
1. **Restructure the evaluation to use a subject-level split** — Train on a subset of subjects, validate on another subset, and test on held-out subjects. This is the only way to measure generalization to unseen individuals. Report both per-subject majority-class baselines and model performance. If performance drops substantially under this split, that is itself an important finding about the difficulty of cross-subject deception detection.
2. **Report simple baselines** — At minimum: majority-class, random, and a simple feature baseline (e.g., logistic regression on eGeMAPS or TF-IDF unigrams).
3. **Disclose details of the emotion recognition model** — Architecture, training dataset, emotion categories, and accuracy. Ideally release the model weights.
4. **Include a separate test set** (not just training and validation).

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>