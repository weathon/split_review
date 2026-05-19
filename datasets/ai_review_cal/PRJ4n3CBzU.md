- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3
Now I have a thorough understanding of the paper and have verified the key claims. Let me write the final review.

## Summary

This paper introduces AttackQA, a 25,335-pair cybersecurity Q&A dataset derived from the MITRE ATT&CK knowledge base, and evaluates a RAG pipeline using fine-tuned open-source models. The core contributions are: (1) a methodology for generating a domain-specific Q&A dataset with automated quality control via a fine-tuned Llama 3 70B model, (2) evidence that fine-tuning both an embedding model (E5 Large V2) and a generation model (Llama 3 8B) on this dataset yields higher correctness on the evaluation set than zero-shot proprietary models (GPT-4o + Text-Embedding-3-Large), and (3) an ablation study isolating the contributions of embedding vs. generation fine-tuning.

## Strengths

- **Fine-tuned embedding achieves substantially higher context recall than a proprietary SOTA embedding**: Table 2 shows the fine-tuned E5 Large V2 attains 92.18% top-5 context recall vs. 80.85% for OpenAI Text-Embedding-3-Large — an 11.33 percentage-point gain. This is a concrete, quantitative result that directly supports a core claim.

- **Fine-tuned Llama 3 8B with tuned embedding outperforms GPT-4o on the evaluation set**: Table 3 reports that the combination of tuned embedding and tuned generation achieves 86.07% hard correctness, compared to 72.38% for the OpenAI pipeline. Even GPT-4o paired with the tuned embedding (79.08%) underperforms the fully tuned open-source setup. This provides clear evidence that domain-specific fine-tuning of smaller open-source models can be effective.

- **Ablation study cleanly separates contributions**: Table 3 isolates the effect of embedding tuning (+15.06 points from base to tuned embedding with the same base generation) and generation tuning (+9.27 points from base to tuned generation with the same base embedding). This structured decomposition strengthens the empirical evaluation.

- **Fine-tuned QC model demonstrably improves filtering over GPT-4o and base Llama 3 70B**: Section 3.4.2 shows the fine-tuned QC model achieves 84.2% precision and 89% recall on the validation set, whereas GPT-4o and the base model essentially predict all positives (trivial strategy with high recall but no discrimination). This validates the automated curation approach.

## Weaknesses

### Major

- **Dataset quality evidence is thin relative to the claim that this is a "high-quality" dataset**: The paper's primary contribution is the AttackQA dataset, yet the only human annotation is 400 pairs (320 training, 80 held out) used to train the QC model. The final 25,335-pair dataset receives no human expert evaluation — no domain-expert spot checks, no inter-annotator agreement, no human evaluation of a random sample. While the QC pipeline (fine-tuned Llama 3 70B with 84.2% precision) and grounding strategies (citations, deduplication) provide partial assurances, the evidence is insufficient to convincingly rule out systematic errors (hallucinations, vague questions, incorrect answers) across 25k+ pairs. This is fixable with additional human validation, but as written, the dataset's quality is not rigorously established.

- **Claims of "outperforming" proprietary models are overstated due to asymmetric comparison**: The paper consistently frames results as fine-tuned open-source models "outperforming" or "surpassing" GPT-4o and Text-Embedding-3-Large (abstract, introduction, conclusion). However, every comparison pits *fine-tuned on AttackQA* models against *zero-shot (off-the-shelf)* proprietary models. That a small model fine-tuned on the evaluation distribution beats a large general-purpose model on in-distribution examples is expected — it demonstrates the value of domain adaptation, not a fundamental model capability advantage. The claims should be scoped accordingly. The underlying results are still valuable, but the framing is misleading.

### Minor

- **No confidence intervals or significance tests reported**: All correctness and recall figures in Tables 2 and 3 are point estimates without uncertainty quantification. With a 2,533-sample evaluation set, many differences are likely significant, but the reader cannot assess which gaps are meaningful (e.g., 82.87% vs. 88.12% in soft correctness). Adding bootstrap confidence intervals would strengthen the quantitative claims at essentially no cost.

- **LLM-as-a-judge evaluation (Llama 3 405B via G-Eval) is not calibrated against human judgments**: The correctness metric, which drives all quantitative conclusions, relies entirely on an automated judge. While the case studies look plausible, no human evaluation is reported on the 2,533-sample evaluation set to establish agreement rates or identify systematic biases of the judge. This means the correctness scores are only as reliable as the judge, and we do not know how reliable that is for this specific cybersecurity Q&A task.

- **No aggregate error analysis**: The paper presents only three illustrative case studies (all positive examples). There is no breakdown of failure modes — what fraction of errors are due to retrieval misses vs. generation errors vs. hallucination? An error taxonomy or confusion matrix would significantly strengthen the evaluation.

- **Retrieval evaluation is effectively closed-set**: The training procedure ensures all documents appear in the training set (Section 4.1), so the embedding model has been exposed to every document it might need to retrieve during evaluation. In a real deployment, new documents would appear, and the model's generalization to unseen documents is not tested. The paper should acknowledge this limitation.

- **"Fully open-source" and "low-latency" claims are imprecise**: The abstract describes "a fully open-source, high-speed RAG and evaluation pipeline" and the introduction claims "an accurate and low-latency end-to-end RAG pipeline." The pipeline relies on SambaNova Cloud's proprietary hardware (SN40L) to achieve the reported speeds. Additionally, no end-to-end latency measurements are reported — only model-level token throughputs (1100+ tokens/s for Llama 3 8B, etc.). These claims overstate what the paper actually demonstrates.

### Trivial

None.

## Nice-to-Haves

- Have domain-expert SOC analysts manually evaluate a random sample of 200–300 Q&A pairs from the final dataset and report the proportion of correct, relevant, and hallucinated entries. This single addition would most directly address the dataset quality concern.
- Calibrate the LLM judge by comparing its scores to human judgments on a subset (e.g., 100 examples) and report agreement rates.
- Add bootstrap 95% confidence intervals to all main metrics in Tables 2 and 3.
- Reframe the competitive claims to state honestly: "After fine-tuning on AttackQA, our open-source pipeline achieves higher accuracy on the AttackQA evaluation set than off-the-shelf GPT-4o and TE-3-L." This is still a valuable finding and does not overreach.
- Include an error analysis section categorizing failure types (retrieval miss, generation hallucination, partial answer, etc.).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Column labels in Table 3 are hard to parse"** — Formatting nitpick; the labels are clear enough.
- **"Reproducibility details missing (random seeds, hyperparameters)"** — The paper provides learning rate, weight decay, optimizer, training steps, and mentions using SambaStudio UI. This is reasonable for a paper of this type.
- **"No discussion of potential biases in the synthetic generation"** — Speculative concern not specifically tied to any concrete evidence in the paper.
- **"Case studies are cherry-picked"** — While the paper could benefit from aggregate error analysis, the case studies are presented as illustrations, not as representative samples. The "cherry-picked" framing is overwrought.
- **Strength about "AttackQA dataset provides a high-quality resource"** — Conflicts with the verified weakness about insufficient quality evidence; the weakness wins per filtering rules.
- **Strength about "Case studies provide qualitative evidence"** — Overstated given the lack of aggregate error analysis.

## Novel Insights

None beyond the paper's own contributions. The combination of embedding fine-tuning + generation fine-tuning with careful ablation on a domain-specific dataset is well-executed but follows established methodological patterns (RAFT, DSS). The key empirical insight — that embedding fine-tuning contributes more to overall accuracy gains than generation fine-tuning in this setting — is clearly surfaced in Table 3 and is the most actionable finding for practitioners building domain-specific RAG systems.

## Suggestions

1. **Most important: validate dataset quality with human expert evaluation.** This addresses the paper's largest evidential gap. Even 100–200 randomly sampled pairs evaluated by a cybersecurity practitioner would dramatically strengthen the dataset contribution.
2. **Reframe competitive comparisons** to explicitly note the fine-tuned vs. zero-shot asymmetry throughout the paper, not just in the evaluation section.
3. **Add confidence intervals** (bootstrap or otherwise) to all main results.
4. **Report end-to-end latency** of the RAG pipeline if claiming "low-latency," or remove the term.
5. **Calibrate the LLM judge** against human judgments on a subset of the evaluation set.
6. **Add an error analysis section** with a breakdown of failure types.
