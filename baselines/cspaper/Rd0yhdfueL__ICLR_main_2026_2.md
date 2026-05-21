---
job_id: e1ee5c43-cf60-427b-824e-c37e228f8df9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Rd0yhdfueL.pdf
paper: Bhav-Net: Knowledge Transfer for Cross-Lingual Antonym vs Synonym Distinction via Dual-Space Graph Transformers
main_score_norm: N/A
desk_reject: true
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning, transfer learning, multilingual language modeling, and graph-based learning for lexical semantic relation classification.

## Minimum Quality
Fail ❌. Although the paper has the expected high-level sections, it contains a central methodological inconsistency that undermines the validity of the model and results: in **Page 5, Equations (13) and (14)**, the model applies `global_mean_pool` over all graph nodes and then produces a single prediction $\hat y$, yet **Equation (15)** defines binary cross-entropy over $N$ labeled samples, implying one prediction per pair. The same inconsistency appears in **Algorithm 1, lines 11–13 (Page 6)**, where a pooled graph representation is used for prediction inside a loop over individual pairs. This is not a minor presentation issue, it makes the training/evaluation formulation internally inconsistent. In addition, the experimental protocol does not specify train/validation/test splits or how hyperparameters and thresholds are selected, which prevents assessing whether the reported results are methodologically sound.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to automated reviewers, or suspicious embedded text in the provided paper content.