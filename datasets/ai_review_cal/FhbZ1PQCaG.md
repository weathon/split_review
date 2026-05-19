- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

The paper proposes DT-Mem, a Decision Transformer augmented with a content-addressable memory module that stores, blends, and retrieves task-specific information to improve generalization and training efficiency. The method builds on Neural Turing Machine-style memory and uses LoRA for efficient fine-tuning of the memory module. Experiments on Atari games and Meta-World compare against MDT, RMDT, PDT, and HDT baselines.

## Strengths

1. **Parameter efficiency demonstrated**: Section 5.4 reports that DT-Mem with 20M parameters achieves generalization "approximately on par" with MDT-200M, and the 50M variant surpasses MDT by 16.7% in human-normalized IQM. This is a concrete claim about 10× parameter reduction.

2. **Training time efficiency**: Section 5.4 reports 4×, 8×, and 32× training time reductions relative to MDT-13M, MDT-40M, and MDT-200M respectively (Figure 4). This is a clear computational efficiency advantage.

3. **Generalization on held-out Atari games**: Table 1 (Section 5.3) shows DT-Mem achieves higher DQN-normalized scores than RMDT in 4 out of 5 held-out games, with 95% confidence intervals reported over 16 random seeds. This supports the claim that the memory module aids zero-shot generalization.

4. **Adaptability via memory fine-tuning**: Figure 5 shows DT-Mem fine-tuned on only 10% of target data consistently outperforms RMDT and MDT across nine unseen Atari games. Table 2 shows DT-Mem beats HDT and PDT on Meta-World with fewer adaptation parameters (147K vs. 2.3M hyper-net parameters).

5. **Training performance improvement**: Figure 6 shows DT-Mem improves over MDT in 13/17 games and over RMDT in 15/17 games, indicating the memory module helps during training.

## Weaknesses

### Fatal
None.

### Major

1. **Meta-World comparison uses non-reproduced baselines with no variance reported**: The paper explicitly states (Section 5.2) that HDT results are taken from the original HDT paper, not from a reproduced baseline. Table 2 reports single-value scores without confidence intervals or standard deviations. The reported improvements (3%, 8%, 3% on training, testing no-FT, testing FT) are modest, and without controlling for experimental conditions (dataset composition, evaluation protocol), these differences cannot be definitively attributed to the method. The paper also does not disclose which Meta-World ML45 tasks were used for training vs. testing, making it impossible to assess distributional representativeness.

2. **Scaling claim lacks reported variance and numeric detail**: The central claim that "DT-Mem with 20M parameters is approximately on par with the 200M parameter version of MDT" (Section 5.4, Figure 3) rests on human-normalized IQM scores presented only in a figure. No numeric values, confidence intervals, or significance tests are provided in the text for this key result. Given that Table 1 shows overlapping confidence intervals could exist (e.g., Alien: DT-Mem at 0.53 vs. RMDT at 0.49), the reader cannot assess whether the scaling parity claim is statistically meaningful.

### Minor

1. **Motivation-evaluation misalignment on "forgetting"**: The abstract and introduction motivate the work through the "forgetting phenomenon" — where training on a new task deteriorates performance on previous tasks. However, the experiments train DT-Mem jointly on multiple tasks (multi-game pre-training), not sequentially. No experiment measures performance on previous tasks after training on new ones. This mismatch between the stated motivation (continual-learning-style forgetting) and the actual evaluation (multi-task joint training) weakens the conceptual framing. The method may be useful for multi-task learning, but the paper should either revise the motivation or add appropriate experiments.

2. **Memory retrieval design choice is under-justified**: The retrieval step (Section 4.1, Step 4) uses the content address w computed *before* the memory update to read from the updated memory M_t, with the justification that "the query information is the same as the input information." While this is a defensible design choice (write-then-read), the paper provides no ablation or analysis showing that recomputing the address after update would not improve performance. The relationship between the two attention computations (addressing in Step 2 and update in Step 3) is also not motivated — the erasing vector εᵉ = w ⊙ (1-β) and adding vector εᵃ = (w ⊙ β)Ŵᵛx use a complement operation on β without explanation of why this specific gating form is chosen over simpler alternatives.

3. **Experimental clarity gaps**: (a) The paper selects 17 Atari games based on alphabetical order and lists the 5 held-out games, but the remaining 12 training games are not enumerated, making it impossible to judge training distribution. (b) The "nine unseen Atari games" used in the fine-tuning experiment (Figure 5) are partially named (KungFuMaster, Robotank, Phoenix, Seaquest) but not fully listed, and it is unclear how they relate to the 17-game subset (are they from outside the 17?). (c) The fine-tuning results in Figure 5 use a log-scaled y-axis, which compresses larger numeric differences and amplifies smaller ones — reporting raw values would be more informative.

4. **No ablation of memory design choices**: The paper does not ablate memory size (number of slots), compare against simpler memory mechanisms (e.g., a single vector or learned slot), or analyze whether the two separate attention computations (addressing and update) each contribute. The loss function (Section 4.3) includes auxiliary reward and return-to-go prediction terms without ablation showing they are beneficial beyond the action prediction loss.

### Trivial
None.

## Nice-to-Haves
- Analysis of memory slot usage (how many slots are actually used, do tasks share slots?)
- Wall-clock time per update step analysis (beyond total training time comparisons)
- Hyperparameter sensitivity analysis for α and λ (the paper states they are not sensitive but shows no supporting experiment)

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Missing Table 4 and Figure 7"**: The text references Table 4 and Figure 7, but the training time information appears to be in Figure 4 ("Model training time") — the garbled reference is a parser artifact. Per instructions, parser-stripped content should not be criticized.

2. **"Missing pseudo-code (Algorithm 1, Algorithm 2)"**: Per instructions, the parser strips appendix/supplementary content from all papers; these exist in the original submission.

3. **"Retrieval step is a conceptual error"**: The critic characterized reusing the old address for reading as a "conceptual error that undermines the claimed content-based retrieval mechanism." This is an overstatement. Using the write address for reading back is a standard design pattern in memory-augmented networks (e.g., Neural Turing Machines read from written locations). The paper explicitly acknowledges the design choice. It is a design that could be suboptimal, but it is not an error. I have reframed this as a Minor weakness (design under-justified) above.

4. **Criticism about missing related works**: Removed per instructions (cannot verify external sources).

5. **Formatting/style nitpicks and typo claims**: Removed per instructions (parser artifacts).

## Novel Insights

The key insight emerging from the review is that the paper's most distinctive feature — using a fixed-size content-addressable memory as an internal module within a Decision Transformer — is neither adequately ablated nor compared against simpler alternatives. The retrieval design (reusing write addresses for reading) is a plausible simplification but one that should be empirically validated. More broadly, the paper would benefit from acknowledging that its framing around "forgetting" / continual learning is aspirational rather than directly tested, and repositioning its contribution as improving multi-task training efficiency and zero-shot generalization via explicit memory.

## Suggestions

1. **Report full numeric tables with confidence intervals** for all key results, especially the scaling comparison (Figure 3) and Meta-World results (Table 2).
2. **Ablate the memory design**: vary slot count, test a simpler single-vector memory, and compare recomputing vs. reusing the read address.
3. **Reproduce the HDT baseline** on Meta-World under identical conditions, or at minimum document all setup differences.
4. **Enumerate the full game sets** used for training, held-out evaluation, and fine-tuning in both Atari and Meta-World experiments.
5. **Either add a continual-learning experiment** (sequential task training with forgetting measurement) or revise the motivation to match the actual multi-task joint-training evaluation.
