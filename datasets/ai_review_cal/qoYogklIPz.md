- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8
Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary

This paper introduces **ELM** (Embedding Language Model), a framework that trains adapter layers to map arbitrary domain embedding vectors (e.g., movie or user vectors from MovieLens 25M) into the token embedding space of a pretrained LLM (PaLM 2-XS). This enables the LLM to generate textual interpretations of those embeddings — describing movies, writing reviews, generating user preference profiles, and even handling hypothetical or interpolated entities. The approach uses a two-stage training procedure (adapter pre-training followed by full fine-tuning) on 24 movie-oriented tasks and a user-profile task, and is evaluated via human ratings (100 raters per task) plus two quantitative consistency metrics.

## Strengths

1. **Concrete architectural contribution for injecting domain embeddings into LLMs.** The paper introduces adapter layers $E_A : \mathcal{W} \mapsto \mathcal{Z}$ that map domain embedding vectors into the LLM's token embedding space, treating them as token-level input. This differs from prior soft-prompt or prefix-tuning methods (which steer model behavior) by enabling the LLM to *interpret* external embeddings from arbitrary domains. (Section 2, Fig. 2)

2. **Novel consistency metrics for evaluating hypothetical entities.** Semantic Consistency (SC) and Behavioral Consistency (BC) address the evaluation gap for embedding vectors that have no ground-truth text (e.g., interpolated or extrapolated entities). SC checks whether generated text re-embeds close to the original embedding; BC tests whether generated text enables accurate behavioral predictions. These metrics are reasonable for the setting where no ground-truth descriptions exist. (Section 3.2)

3. **Two-stage training procedure with explicit justification.** The paper separates adapter training (frozen LLM) from full fine-tuning, noting that training continuous prompts poses convergence challenges. This design is sensible and distinguished from single-stage alternatives. (Section 2, "Training Procedure")

4. **Generalization of CAVs to interactive, language-based exploration.** The paper uses trained linear CAVs to extrapolate movie and user embeddings along attribute directions (e.g., "funnier") and shows ELM generates coherent narratives consistent with those attribute shifts, measured by SC and BC. This extends CAVs from a static diagnostic tool to a mechanism for dynamic, language-based exploration of embedding spaces. (Section 4, "Generalizing Concept Activation Vectors", Figs. 4–5)

## Weaknesses

### Fatal

None. The paper's core claims — that ELM can be trained to interpret domain embeddings and generate meaningful textual outputs — are supported by the presented evidence. The framework, training procedure, and basic evaluation are sound enough to warrant consideration. No identified issue invalidates the central contribution.

### Major

1. **Behavioral Consistency (BC) for movie tasks is not defined.** The paper formally defines BC only for the user-profile task (Eq. 2, line 170–174), where it measures whether a generated user profile can rank movies by predicted preference (using a DLM-based ranker). Yet Table 1 reports BC values (labeled "Rank Corr.") for **all 24 movie tasks** — including tasks like "summary," "positive review," and "similarities" — with no explanation of the computation. Movie tasks use *semantic* embeddings (not behavioral embeddings), and the paper never specifies: what ranking is being compared, what constitutes the ground-truth ranking, or how the ranker $\rho$ is applied to movie outputs. A full column of the primary results table is therefore uninterpretable. The authors must either clarify the BC protocol for movie tasks or remove those values.

### Minor

1. **No baselines that also use the embedding.** The paper compares ELM only against text-only LLMs (PaLM 2-L, GPT-4) that lack access to the embedding. This comparison is informative — it shows embeddings encode information beyond what text-only models can access from movie titles alone — but it cannot isolate whether ELM's specific architectural choices (adapter + two-stage fine-tuning) are necessary or beneficial. Baselines using the same embedding (e.g., a simple MLP decoder, an LLM with prefix tuning conditioned on the embedding, or the first-stage adapter alone without fine-tuning) would help attribute results to the proposed design.

2. **SC is reasonable but unvalidated against ground-truth text.** SC measures consistency in embedding space (re-embedding ELM's output and checking similarity to the input embedding). The paper frames this as a metric for hypothetical entities where ground truth doesn't exist, which is a valid use case. However, the paper does not report how SC correlates with human judgments or compare against automated metrics (e.g., BERTScore against actual plot summaries) on a subset of real movies. It is therefore unclear how much high SC reflects genuine semantic extraction vs. exploitation of smoothness in the DLM embedding space or memorization of the teacher LLM's style.

3. **No confidence intervals or inter-rater reliability.** The human evaluation uses 100 raters per task (Table 1), yet only point estimates are reported. Similarly, SC and BC are reported as point estimates without variance. Inter-rater agreement metrics (e.g., Krippendorff's alpha) and confidence intervals would substantially strengthen the quantitative claims.

4. **No discussion of limitations.** The paper does not acknowledge known limitations: the training targets are generated by PaLM 2-L (the same model family as the base LLM), introducing potential distillation artifacts rather than ground-truth semantics; the assumption that the domain embedding space aligns well with the DLM's embedding space; or the potential for hallucination when describing hypothetical entities far from the training manifold.

### Trivial

None.

## Nice-to-Haves

- **Ground-truth comparison.** For a subset of movie tasks, compare ELM outputs against human-written plot summaries or reviews using standard text similarity metrics. This would directly validate whether ELM extracts embedding-specific information beyond what the teacher LLM can generate from the movie title alone.
- **Test on additional domains.** The paper claims generality for arbitrary embedding spaces but only tests on MovieLens 25M. Demonstrating on one additional domain (e.g., product embeddings, protein embeddings) would significantly strengthen the generality claim.
- **Statistical significance.** Report confidence intervals for SC, BC, and human evaluation scores.

## Removed Points

*These points were flagged in the reviews but are removed per the consolidation rules. They are listed here for completeness and should be treated with caution.*

- **"SC is circular and uninformative."** The Harsh Critic claimed SC uses the same DLM for embedding and re-embedding, making it circular. This overstates the issue: SC is a *consistency* metric, not a ground-truth metric. It tests whether ELM's output, when re-embedded, returns to a similar region of the DLM space — a reasonable minimal sanity check for hypothetical entities. The paper also provides independent human evaluation. SC is a useful auxiliary metric, not a circular one. Demoted from "fatal" to the Minor observation above.

- **"Comparison to text-only LLMs is unfair / not a meaningful baseline."** The Harsh Critic argued this comparison merely shows "having access to the embedding helps." However, the comparison is meaningful for its purpose: text-only LLMs receive movie *names* (which they know from training), while ELM receives only an embedding vector. That ELM still outperforms on embedding-consistent outputs demonstrates the embedding encodes information not available from textual knowledge alone. The critic's call for "embedding-access baselines" is a valid *additional* comparison (now a Minor weakness), but the existing comparison is not unfair. Removed as an overstated criticism.

- **"No ablation or comparison to simpler alternatives."** Kept but demoted to Minor weakness #1 (no baselines that also use the embedding). The original framing as a critical/structural issue is too severe — the paper's main contribution is the overall framework, and ablation studies, while valuable, are standard practice for strengthening rather than requirements for validity.

- **"Reproducibility details missing (learning rates, adapter dimensions, optimizer, training data size)."** Removed per the hard rule: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details, or large artifacts impractical to include in a submission." The paper reports key details: two-layer MLP adapter, 20k + 300k iterations, batch size 32, PaLM 2-XS, 1000 test/rest training examples.

- **"Missing related work on decoding embeddings into natural language."** Removed per the hard rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."

- **Strength Finder strength #3 ("Empirical superiority over text-only LLMs") — claim that comparison is clean.** This strength partially conflicts with the verified weakness about baselines. The comparison is informative for showing embedding value but incomplete for demonstrating architectural superiority. The strength is retained in tempered form in the summary.

- **Strength Finder generic/superficial strengths.** Dropped strengths that were generic (e.g., "this paper addressed an important problem") per the filtering rule.

## Novel Insights

The reviews surface an interesting tension in how to evaluate "embedding interpretation" systems. The Harsh Critic demands ground-truth textual validation (plot summaries, human-written reviews), which would test whether ELM extracts *embedding-specific* information that the teacher LLM doesn't already know from the movie title. The paper's SC metric tests a different proposition: whether ELM's output is *consistent* with the embedding (re-embedding yields similar vectors). These are complementary but not equivalent — a model could pass SC by learning to invert the DLM's embedding function while still saying nothing about the actual entity. The most impactful path forward would be a controlled experiment that disentangles the embedding's contribution from the teacher LLM's parametric knowledge, e.g., comparing ELM's outputs for real embeddings vs. random vectors from the same distribution, or testing whether ELM can recover information that is present in the embedding but absent from the teacher LLM's training data.

## Suggestions

1. **Define or remove the movie-task BC column.** This is the most critical issue. Either specify the BC computation protocol for each movie task (what is ranked, what ground truth is used, how $\rho$ is applied) or remove those values from Table 1.

2. **Add at least one baseline that also receives the embedding.** A simple MLP + frozen LLM (stage 1 only, no fine-tuning) or a learned prefix tuning baseline would help isolate the benefit of the two-stage approach.

3. **Report confidence intervals** for all metrics in Table 1 and Figures 2–5, and inter-rater agreement for the human evaluation.

4. **Validate SC against ground truth.** For tasks on real movies, report how SC correlates with BERTScore against human-written plot summaries, or show that SC distinguishes real movie embeddings from random embeddings.

5. **Add a limitations paragraph** acknowledging the dependence on the teacher LLM for training targets, the single-domain evaluation, and potential hallucination risks.
