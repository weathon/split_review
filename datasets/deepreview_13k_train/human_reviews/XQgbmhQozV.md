# Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
\emph{\emph{Warning}: this paper contains model outputs exhibiting unethical information.}
Large Language Models (LLMs) have achieved significant breakthroughs, but their generated unethical content poses potential risks. Measuring value alignment of LLMs becomes crucial for their regulation and responsible deployment. Numerous datasets have been constructed to assess social bias, toxicity, and ethics in LLMs, but they suffer from \emph{evaluation chronoeffect}, that is, as models rapidly evolve, existing data becomes leaked or undemanding, \emph{overestimating} ever-developing LLMs. To tackle this problem, we propose GETA, a novel \emph{generative evolving testing} approach that dynamically probes the underlying moral baselines of LLMs. Distinct from previous adaptive testing methods that rely on static datasets with limited difficulty, GETA incorporates an iteratively-updated item generator which infers each LLM's moral boundaries and generates difficulty-tailored testing items, accurately reflecting the true alignment extent. This process theoretically learns a joint distribution of item and model response, with item difficulty and value conformity as latent variables, where the generator co-evolves with the LLM, addressing chronoeffect. We evaluate various popular LLMs with diverse capabilities and demonstrate that GETA can create difficulty-matching testing items and more accurately assess LLMs' values, better consistent with their performance on unseen OOD and i.i.d. items, laying the groundwork for future evaluation paradigms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In traditional evaluation, given a static benchmark, all evaluation samples are treated equally and evaluated on all samples, potentially exposing these test instances and essentially making these instances i.i.d. over time. The authors call this the chronoeffect. To mitigate these challenges, the paper proposes a dynamic evaluation method where samples in a test set are selected based on the competency (trait) of the language model (LM) being tested. The basis of this method comes from Item Response Theory (IRT). In traditional IRT, the difficulty and discrimination of a sample are hand-coded or provided by templates, whereas the paper relies on an item generation method that treats these as latent variables and optimizes the likelihood of (x, y) over the trait and latents for the given datasets. Moreover, this generation method is further enhanced to take into account unseen difficulty instances, thereby going beyond the static datasets provided for optimization.

### Strengths
1. An important evaluation problem with methods backed up with theories from pyschometrics.
2. Extensive evaluation of multiple models and datasets.

### Weaknesses
The paper is quite dense. For me and most of the audience at ICLR, it would be hard to follow unless they are working in IRT and optimization.

I wish the underlying equations and methodologies were grounded in examples to make the intuition clear.

It is unclear to me why the resulting trends proposed by the evaluation method should be trusted without a ground truth. Some synthetic evaluation settings could make these results more trustworthy.

### Questions
How does this address the chronoeffect when the underlying test set is essentially the same, i.e., the evaluation method is not going to generate examples beyond the given test set? Is it the case that since not all samples are exposed, this could help mitigate the chronoeffect?

How do you know if the resulting results can be trusted? Is there a synthetic problem where the results can be compared to the ground truth?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose GETA, a method for identifying model evaluation boundaries and generating new/difficult examples to evaluate a set of models on. GETA consists of jointly training a Variational IRT model (implemented as a simple Transformer) and an item generator (fine-tuned LLaMA-3). They evaluate on various toxicity/ethics/bias datasets, and claim that this approach can help to address evaluation data leakage/difficulty concerns.

### Strengths
- The paper is clear and in-depth in its description of the method. The evaluation and experiments are presented exceedingly clearly.
- The approach is well-motivated and reasonable, though I have some concerns mentioned below.

### Weaknesses
 - It is not clear why "alignment" (toxicity/bias/ethics) datasets were chosen in particular for evaluation GETA, which appears general enough to be applied to any problem (I presume mostly bottlenecked by the ability of the IRT estimator and generator, but it's not clear to me that alignment would be less challenging than some other domain, e.g. math, code)
- Additionally, I would have wanted to see more experiments with different generators. This would both help address my question above (what is the bottleneck) as well as help to investigate any model-model interactions (would generators from certain families create problems easier for models in the same family?)
- Additionally, I am curious about the viability of generating difficult problems, especially when the generator chosen is weaker than many of the models evaluated. Does the joint model generate truly difficult problems, or find edges of the evaluated models' ability. Are there domains where the generator struggles to generate reasonable and challenging problems? Addressing this set of concerns would go a long way to further convincing me of the broader viability of this approach..

### Questions
- Some of my questions are mentioned above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper aims to measure the value alignment of language models using psychometric testing theory. In particular, it highlights that static datasets that measure bias, toxicity, and ethics of language models can be contaminated, as models are trained on the outputs. In response, the paper draws from methods in computerized adaptive testing to adaptively generate tests for the model. To generate tests, the paper uses an IRT model parameterized by a two-layer transformer to model the difficulty of an item, then selects items out of an item pool. The item pool is filled with “items” that are generated adaptively by fine-tuned Llama 3 8B. The paper then validates this method for testing model’s ethical judgements by comparing how it ranks eight different models, and argues that its method produces qualitatively better judgements, and matches existing leaderboards (like the Enkrypt AI safety leaderboard).

### Strengths
* This paper helps address an important problem in language model evaluation — static benchmarks can enter subsequent training sets, and lose signal
* GETA can generate examples at different difficulty levels, circumventing some problems with adaptive adversarial evaluation that will almost always provide failures (and thus not provide useful features for comparison)
* The paper evaluates GEPA on multiple aspects of value alignment (bias, ethics, toxicity)

### Weaknesses
 * The primary weakness is the evaluation of GETA; GETA is evaluated either based on subjective intuition about how language models should rank on different value alignment tasks or exogenous benchmarks. In order to claim that GETA actually makes progress, it’s critical to measure how it compares to direct human judgment of these models in a way that cannot be contaminated.
* The method introduces a lot of complexity, such as variational item response theory, when simpler baselines exist (in particular, since items are already being generated by language models, there should be prompting baselines such as generating lots of questions with varying difficulty and comparing model responses to human responses); it’d be nice to better understand which parts of the framework are necessary (since traditionally in deep learning, hard-coded assumptions with smaller models tend to lose out in the limit).

### Questions
* My impression from reading the paper is there isn't a human study validating that GETA better ranks models. Is this the case, and if so why should trust other sources for ground truth (when they could be contaminated, or biased by other processes)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors present a novel method called GETA (Generative Evolving Testing of vAlues) to generate test hard test instances and concurrently estimate the degree of conformity of the model to the values being tested. The motivation is tackling what they call the evaluation chronoeffect challege, i.e. the saturation of benchmark performance due to leakage or increased LLM performance. 

Their approach jointly trains of a Variational IRT (Item Response Theory) model (capturing conformity and item difficulty) and an item generator with a clever ELBO setup. Using a model as an item generator allows them to avoid having to rely on a large item pool to select from. The estimated conformity is directly used to assess model performance.

The authors compare their method with vanilla testing on the static evaluation and two different test selection approaches. They compare the correlation between their Value Conformity scores and the scores available in publicly available leaderboards, which are massive compared to the ~100 items considered in GETA evaluation.

### Strengths
- The paper offers a novel combination of ideas from the literature, addressing a real issue.
- The joint modelling of item difficulty, model conformity and item generation is very neat and likely to be usable beyond the ethical value assessment
- The paper (including the appendix) is a very nice writeup that documents very thoroughly the approach
- If the experimental claims are to be trusted, the authors are mostly reproducing larger (but how much larger) leaderboards with ~100 instances.

### Weaknesses
 - The presentation is very dense, and because of this it's sometimes hard to get some details. For example, I failed to understand how is the AIG generator conditioned on item difficulty. See my suggestions in the "Questions" setting
- For a paper that discusses the chronoeffect evaluation challenge, there is little experimental discussion of time. I would have liked to see whether there would be any discernible difference when testing model before and after a cutoff date (e.g. a dataset release), with GETA vs SE. (The focus is on, so to speak, "interpolation", but this paper would benefit a lot from more focus on "extrapolation": identifying failure modes of current evaluations, and showing that their method alleviates or solves these issues)
- The claim that correlation with leaderboards is the best signal of evaluation quality is not the strongest. I understand that this is a hard problem, but it would be good to include some more discussion about it, i.e. on why the leaderboards are reliable at all.

### Questions
- It would be **very** helpful to rework the notation a bit. The notation is at time confusing, e.g. having $y$ as the response score and $y^*$ as the ground truth answer. Other possible improvements are the double indexing in $y$, and the parameters denoted as $\theta$, $\psi$, $\phi$. Also the notation is very rich in symbols and the reader is seldom if ever reminded of what they mean. Note that none of this would be a problem in isolation, but all together this makes the paper needlessly hard to follow.

### Soundness
2

### Presentation
2

### Contribution
2
