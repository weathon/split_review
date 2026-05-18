- Decision: Reject
- Scores: 5, 3, 3, 3

## Merged Review

### Summary
The paper studies pre-training dynamics of a 125M-parameter GPT-2 model on a novel first-order logic (FOL) dataset (2.5B tokens), aiming to test whether observations from small-scale algorithmic tasks (e.g., grokking) transfer to larger, more realistic setups. The authors generate FOL tautologies synthetically (400–500K syntactical rules) and instantiate them in natural language using off-the-shelf LLMs. They evaluate generalization on multiple validation sets including Dyck grammars and human-curated datasets (Folio, LogicBench). By inspecting training/validation loss curves and mean eigenvalues of OV and QK matrices, they claim distinct phase transitions corresponding to hierarchical learning of operators and rule sets. Reviewers acknowledge the dataset contribution and the goal of bridging small-scale mechanistic studies and large-scale realism, but raise significant concerns about clarity, rigor, and conclusiveness. One reviewer (score 5, confidence 4) is substantially more positive than the others (scores 3), praising the scale and timeliness, while others find the findings provisional, unsupported by evidence, and lacking proper hypothesis testing.

### Strengths
- The approach of using a synthetic pre-training dataset of first-order logic (FOL) at 125M parameters and 2.5B tokens is timely for testing whether observations from small-scale studies translate to larger scales (Reviewer 1).
- Efforts to conduct the synthetic study at a scale larger than typical mechanistic interpretability studies are appreciated (Reviewer 1).
- Originality: transformers have not been tested in a similar explicit FOL setting at this scale with 400–500K syntactical rules. The use of multiple generalization tests (human reasoning datasets, Dyck grammars) helps the work stand out (Reviewer 2).
- Quality: experimental design is appropriate and strengthened by multiple generalization tests, eigenvalue analysis of attention matrices, and verifiability of the FOL and Dyck tasks (Reviewer 2).
- Clarity: the paper is well written and easy to follow, well motivated, and placed within the broader literature (Reviewer 2; note: this positive clarity assessment contrasts with other reviewers).
- Significance: obtaining an understanding of how transformers learn FOL is a clear advance that could lead to further work; the new dataset could be reused (Reviewer 2).
- The paper focuses on an important and relevant problem of generalization in LLMs (Reviewer 3).
- Using first-order logic is a reasonable middle ground between simple models of computation and natural language (Reviewer 3).
- The generated dataset (FOL statements synthetically generated and proved valid, then instantiated in natural language by LLMs) might be a valuable asset for the community (Reviewer 3).
- Generation of complex synthetic datasets as a formalized subset of natural language is a potentially useful tool for understanding training dynamics and systematically evaluating shortcomings of language models at smaller scales (Reviewer 4).

### Weaknesses
**Clarity and presentation**
- Main result figures (Figures 2–6) are loss curves with many lines and only single-sentence captions; no formal definition of “phases” is given – they appear to be drawn subjectively (Reviewers 1, 2). Phase 6 in Figure 2 has no clear salient point (epoch 140) and is not explained (Reviewer 2).
- The description of the FOL task is vague: it is never specified how much of the text is shown to the model (e.g., everything up to the final →?) and what the model must output (Reviewer 2). The Dyck grammar setup is similarly unclear: how input is presented and what output is required (Reviewer 2).
- Figures suffer from small font sizes, indistinguishable lines (e.g., Figure 3a has two blue dotted lines), and vague captions that do not explain the numbered transitions (Reviewers 1, 2). Loss plots should be reported in log scale (Reviewer 4). Table 1 examples need spacing for readability (e.g., ∀ x AttendParty(x)) (Reviewer 2).
- The writing does not tell a clear story; claims are post-hoc, based on visual inspection of noisy training curves, with no attempt to formally investigate, suggest alternative hypotheses, repeat experiments, or form a unifying theory (Reviewer 3). Both the form and substance make it difficult to obtain a clear conclusion (Reviewer 3). The presentation of empirical results lacks clarity on concrete findings and their implications (Reviewer 4).
- The statement “Furthermore, we create… test of generalization” (lines 180–183) is unclear, coming abruptly after the Dyck description (Reviewer 2).
- The authors assume causal next-token prediction cross-entropy loss but do not state this explicitly (Reviewer 4).

**Experimental rigor and reproducibility**
- The central findings are “suspicions” rather than confirmation of falsifiable hypotheses; hypotheses are not formulated cleanly (Reviewer 1).
- Learning transitions are never formally defined; the inflection point in Figure 3 is not convincingly meaningful – all depth trajectories follow almost the same path except m1, and that gap appears in only one task setting with no notion of variance (Reviewer 2). By phase 6, shallow and deep expression losses overlap (Reviewer 2).
- Figure 7a claims copying behavior only emerges in the first layer, but later layers have non-negligible copying magnitude if negative eigenvalues are considered (Reviewer 2). Figure 5 claim that brackets are learned before any other symbol is not supported: all symbols appear to begin learning immediately and converge at similar times (Reviewer 2). Figure 6 dynamics differ from Figure 5, raising concerns about the connection to phases in Figure 2 (Reviewer 2).
- There is no analysis of stability across seeds, data ordering, model sizes, or optimization hyperparameters; phase transitions could be random fluctuations (Reviewer 4).
- The paper reports only loss, not a more interpretable metric such as accuracy of masked FOL predictions, making it hard to judge task difficulty and model performance (Reviewer 4). The task difficulty is not compared to other algorithmic datasets (Reviewer 4).
- Training is done for only 10,000 iterations, whereas the default nanoGPT training is 600,000 iterations; the connection to grokking is dubious since the original grokking paper required up to 1000× longer training for a much smaller model (Reviewer 3). No model in this work actually groks (Reviewer 2).
- The relation to double descent is misapplied: double descent concerns the number of parameters, not training time or epochs (Reviewer 2).
- There is a false statement in Appendix A: the Universal Instantiation rule is given incorrectly (∀_x P(x) implies P[x/t] for all t, not as written) (Reviewer 3). The discussion incorrectly distinguishes propositional logic (including all connectives) from first-order logic (adding predicates and quantifiers) (Reviewer 3).
- The term “semi-algorithmic” for FOL is not justified; FOL statements can be algorithmically evaluated (Reviewer 4).

**Dataset concerns**
- The novel dataset is generated from LLMs, but little concern is given to the unreliable nature of this approach; it is presented as ground truth without scrutiny, though mitigated somewhat by the human validation set (Reviewer 2). It is unclear what LLM-generated data adds beyond purely symbolic generation in SymPy, which gives verifiable control over the data distribution (Reviewer 4).
- If Folio and LogicBench are used to generate data as in-context examples, there may be data leakage into the validation set; no control is mentioned (Reviewer 4).
- It would be possible to only include syntactical rules verifiably not covered by the train set, but this is not done (Reviewer 4).

**Generalization claims**
- The generalization experiment with Dyck grammars is unconvincing: Dyck is a subset of FOL, so it tests a prerequisite rather than true generalization; the high loss on Dyck shows poor generalization, yet the paper claims the model generalizes at scale (Reviewers 2, 4). The connection to out-of-domain generalization is not justified (Reviewer 4).
- Claims about shallow vs. deep expressions exhibiting differential losses are not supported: all lines overlap by phase 6 (Reviewer 2).
- The central claims are purely post-hoc and no attempt is made to explain the difficulty of learning different FOL rules (e.g., from computational complexity) or to make predictions for future experiments (Reviewer 3). Why not start with propositional logic as the next step after Dyck languages? (Reviewer 3)
- There is no discussion of limits of transformer-based logic reasoning, analogous to Yao et al. for limited-depth Dyck languages (Reviewer 3). The paper should test systematic/compositional generalization to novel compositions of seen FOL expressions (Reviewer 4).
- The relationship to recent works on hierarchical generalization in transformers pretrained on formal language data (e.g., PCF(S)G) is not discussed (Reviewer 1). Analysis of learned representations through the lens of formal grammar theory is missing (Reviewer 1).
- The link between OV/QK circuit formation and phase transitions is speculative; no concrete predictions or verification are provided (Reviewers 1, 2).