# Can Large Language Models Reason? A Characterization via 3-SAT

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Large Language Models (LLMs) have been touted as AI models possessing advanced reasoning abilities. However, recent works have shown that LLMs often bypass true reasoning using shortcuts, sparking skepticism.
To study the reasoning capabilities in a principled fashion, we adopt a computational theory perspective and propose an experimental protocol centered on 3-SAT -- the prototypical NP-complete problem lying at the core of logical reasoning and constraint satisfaction tasks.
Specifically, we examine the phase transitions in random 3-SAT and characterize the reasoning abilities of LLMs by varying the inherent hardness of the problem instances. Our experimental evidence shows that LLMs are incapable of performing true reasoning, as required for solving 3-SAT problems. Moreover, we observe significant performance variation based on the inherent hardness of the problems -- performing poorly on harder instances and vice versa. Importantly, we show that integrating external reasoners can considerably enhance LLM performance. By following a principled experimental protocol, our study draws concrete conclusions and moves beyond the anecdotal evidence often found in LLM reasoning research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper analyzes the algorithmic reasoning abilities of LLMs via the 3-SAT problem. The authors examine performance on instances of varying hardness as characterized by the phase transition of random 3-SAT. They test the LLM on three kinds of prompt: a representation of an integer CNF formulation, a natural language translation of the same, and a prompt that just asks the LLM to translate a natural language instance into LaTeX. They find that LLMs fail to robustly solve these problems, and SoTA systems perform worse on harder problems, but that--across many models--performance is much lower than the phase transition analysis would imply in high alpha regions.

### Strengths
1. Contrasting previous work, the authors clearly define which notion of "reasoning" they are examining and choose a canonical, well-studied classical problem to examine LLM performance on. 
1. The introduction does a good job of covering most of major, relevant LLM reasoning-related previous work, situating the current work in the landscape of both positive and negative results.
1. The authors construct their evaluation set using a strong, well-studied random sampling procedure for 3-SAT problems, ensuring the distributional validity of their results, and allowing for more detailed analysis grounded in previous work.
1. The authors analyze much more than just accuracy, considering not only performance around the critical region, but also relative to another proxy for difficulty: the satisfiability ratio, thus strengthening their results.
1. The authors demonstrate how to boost performance in some cases by combining the LLM with an external solver.
1. The authors do their tests across a number of different models.

### Weaknesses
## Issues with Natural Language Prompt formulation
  
If I'm interpreting the SAT-MENU prompt correctly, then I believe it violates commonsense. The prompt asks for a list of orderable and a list of non-orderable foods that satisfies a group of people, or equivalently an assignment of "orderable" or "not orderable" to each food in a pre-specified list of foods. The immediate assumption is that satisfying this group of people has something to do with the actual act of ordering foods for the group somewhere down the line, e.g. that these lists will be used for ordering later on. However, given this or a similar assumption, the problem specification leads to some rather absurd possibilities. 
  
Consider "Jay dislikes pizza, pie, and nachos. Mary likes pizza and pie, but dislikes nachos." Is there an orderable list and non-orderable list which satisfies both Jay and Mary, using only pizza, pie, and nachos? A commonsensical answer would be no, because Jay doesn't like anything on the menu, but the structure of the problem is such that Jay is happy as long as one of the things he doesn't like isn't ordered. In particular, we have the following absurd-looking satisfying assignment: "orderable: nachos, pie. non-orderable: pizza" in which Jay is happy because pizza isn't orderable; whereas nachos, disfavored by both, *are* orderable. I know this is somewhat subjective, but this makes SAT-MENU more of a syntactic sugaring of the CNF prompt rather than a natural example of somewhere where this kind of reasoning needs to be done.
  
This likely speaks to a broader issue with the representations used here. The CNF formulation is a modeling convenience rather than a natural framing of real-world problems (see e.g. Stuckey 2013 "There Are No CNF Problems"). Analyzing SAT-CNF makes sense if we are interested in how well LLMs have acquired the ability to solve classical 3-SAT problems. SAT-MENU is the same problem with added distractors. Neither of them are well-justified as proxies for the kinds of natural language constraint satisfaction queries we might expect LLMs to actually be asked to solve. I would appreciate if the authors would clarify if the goal is to examine average-case reasoning performance (as alluded to in line 444) or to demonstrate the existence of a domain on which LLMs clearly fail to reason and resort to statistical shortcuts. If it is the former, I would be interested in seeing more plausible prompt reformulations.

## Complexity Class Claims
At lines 90-91 and 151, the authors claim that "logical reasoning, planning, and constraint satisfaction" can be reduced to 3-SAT. This is only true for limited forms of logical reasoning, e.g. the decision problem for first-order logic is in fact undecidable. Furthermore, planning also cannot in general be reduced this way: just the problem of plan existence (in STRIPS planning) is already PSPACE-complete. Note however that the (easier) *scheduling* phase is generally reducible to constraint satisfaction.

## Unclear Relationship to Cited Paper: Kambhampati 2024a
Lines 138-140 do not seem to match section 5.2. Emphasis mine:

> Additionally, we demonstrate how integrating LLMs with external **verifiers**, such as in the LLM-Modulo Frameworks (Kambhampati et al., 2024a), can enhance reasoning capabilities and improve performance on 3-SAT problems

Line 350 restates the claim:

> "The main idea is to augment LLMs with **critics and verifiers** (Lightman et al., 2024; Hazra et al., 2024b), recognizing the ability of LLMs as approximate idea-generators for problems as against directly solving them"

These quotes accurately reflect the LLM-Modulo framework as described in Kambhampati 2024a (quote from p6 of that paper): 

> "LLM-Modulo architecture is a 'Generate-Test' one that involves LLMs interacting with the external critics/verifiers **rather than a LLMs being just frontends to external solvers**" 

However, lines 355-356 describe the setup the authors tried in this paper, which contradicts both their previous summaries of their own work as well as the main idea of the framework they claim to be implementing. Section 5.2 describes how to use the LLM as a syntactic translator from the SAT-MENU format into one that MiniSAT can process, rather than using the LLM as a generator for proposed answers that are then filtered through sound verifiers/critics. Because of the problems presented (which are essentially already in CNF form) and the SAT solver in the loop, this seems to be a noisier analysis of the ability for the LLM to do syntactic translation, and doesn't tell anything about reasoning. (I say noisier because there is a chance that the generated translation was incorrect, but happened to have a satisfying assignment that also satisfies the real problem.)

If the authors are interested in the LLM-Modulo framework, perhaps one approach would be to compare how many generate-test iterations it takes for the model to output a satisfying assignment relative to the alpha region.

## Other Citation and Unclear Claim Issues/Nitpicks
1. The paper states that "emergent abilities have been shown to emerge" in line 39, but later (line 83) cites a paper claiming that emergent abilities are "a mere mirage," making the authors' position unclear.
2. Lines 80-81 cite Dziri 2023 for a claim about architectural limits of transformer layers, but that paper is an empirical evaluation of pre-trained models together with some (very broad) theoretical claims that are applicable to any autoregressive model, not just transformers. This citation doesn't seem to be relevant here and should likely be removed.
3. Line 182-183: Olausson 2024 and Liu 2023 are cited in the context of combining LLMs with verifiers and heuristics, but the systems proposed in those papers (LINC and LLM+P) combine translator LLMs with *solvers*, not verifiers. It's unclear why Lightman 2024 is cited, as it seems to be about process supervision at train time, rather than combining an LLM with a verifier at inference time.
4. Line 340: in-text citation was incorrectly formatted (citet should be citep).
5. The final paragraph of the conclusion (line 468-471) makes claims that seem unrelated to and unexamined by the content of the paper's body.

### Questions
1. I notice that, in figure 3, GPT-4 seemingly significantly worse than random guessing on the SAT decision problem around the critical point (which would imply for instance, that taking the opposite of its answer would be a better algorithm for the decision problem, giving about 70% accuracy right at alpha). Is this effect consistent/significant/predictable? Have the authors looked at why this is?
1. Given that these prompts are CoT prompts, have the authors looked at what sort of procedure the LLM claims to be following (and if it matches with the given examples)? Specifically, I'm curious if we can distinguish the LLM results from what we would get if instead we tested a noisy reasoner--a very simple example would be an implementation of DPLL where every each search step has some fixed epsilon probability of failure.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study the reasoning capabilities of various LLMs by studying how well they can solve the Boolean satisfiability problem. The authors consider two different encodings of 3-SAT instances to be given as input to LLMs. An encoding to a natural language problem (they construct a problem related to a group of people ordering food items with given constraints) and by directly imputing formulae in 3-CNF to the LLMs.

They generate several datasets of CNFs by using different fixed parameters for the ratio of the number of clauses and variables. By varying this constant the authors can control the proportion of satisfiable formulae in their datasets.

They also consider the task of using LLMs to transform inputs in their format to a format understandable by a SAT solver.

In general, they find that LLMs cannot solve 3-SAT, but that they can transform inputs in their format to a format understandable by a SAT solver.

### Strengths
It is worthwhile to experimentally test the limitations of LLMs via problems arising from complexity theory. I liked the fact that the authors consider the phase transition related to 3-SAT. The discussion on related works is thorough.

### Weaknesses
The results are not surprising, as in general, current LLMs are not expressive enough (as mentioned by the authors) to decide 3-SAT. Moreover, LLMs have been recognised to be successful in transforming formats of diverse data, and hence it comes with no surprise that the integration of LLMs with SAT-solvers is successful. In summary, the authors only test how well various LLMs can solve 3-SAT. This kind of work is an excellent topic for a student project, but in my opinion does not suffice to be publishable in a top machine learning conference. 

There is not much theoretical contribution in the submission. While it is natural to consider 3-SAT as a problem to solve and to use different encodings to LLMs, there is nothing theoretically novel there. The technical contribution is to generate these inputs (taking the phase transformation of 3-SAT in mind) and tabulate the results with respect to different LLMs. I do not think that these contributions suffice for a publication in a top general conference in machine learning.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This papers studies the question of whether LLMs can reason. Towards this question the authors propose a new method for studying reasoning capability, by evaluating the performance of LLMs in deciding satisfiability of 3-SAT instances.

This is motivated by a classic observation on the likelihood of random 3-SAT instances being satisfiable or unsatisfiable depending on the ratio alpha of clauses to variables in the instance. When alpha is low, the instance is almost surely satisfiable, and when the ratio is high, it is almost surely unsatisfiable. In the middle, there is a small range of this ratio where the satisfiability of random 3-SAT instances is hard to predict from statistical information.

The authors then compare this behaviour to the performance of various LLMs on random 3-SAT instances. As their key finding, they observe that the performance of GPT-4 is much better in the case of low or high alpha, suggesting that the LLM answers based on statistical/structural information rather than reasoning.

### Strengths
- The paper proposes an approach beyond the common toy-like example based evidence often found LLM reasoning research and provides well-founded analysis of reasoning in LLMs. Beyond the 3-SAT   based analysis in particular, the general approach has potential to crate a broader range of LLM reasoning benchmarks. As such the submission could be important to this emerging area of research.

- As a secondary result, the submission demonstrate that LLMs are very capable of translating 3-SAt instances in textual form into input to SAT solvers. Although there is a small gap in the paper here in that it is not clear what happens when the input in the SAT-Menu format is provided that is not restricted to clauses with at most 3 terms, i.e., when it would be a general SAT instance beyond 3-SAT.

- The presentation is clear, the claims and methods are easily followable.

### Weaknesses
 - The paper claims that these results counter previous works that suggest reasoning ability in LLMs. However, the results of this submission suggest that LLMs are effectively unable to reason about an NP-hard problem. Previous positive results such as those by Kojima et al. (2022) are on inherently simpler problems. The paper lacks an appropriate discussion on this mismatch and the role NP-complete problems in the current discourse on LLM reasoning ability.

- As mentioned above, I find the approach itself promising. But the paper lacks any discussion of building on this approach to provide a more complete picture on LLM reasoning limits. For example, it would be a natural next step to demonstrate similar behaviour of LLMs also for problems in lower complexity classes. But there is no discussion along these lines nor an attempt to frame the approach in a general fashion.

- The set of tested models seems slightly outdated for this submission cycle (GPT 4 Turbo, Gemini 1.0, Llama 2).

### Questions
- Why are instance in the dataset annotated with the number of satisfying models rather than just SAT/UNSAT information? 

- Have you considered extending this approach by any problems beyond 3-SAT? While I understand that the phase transition on random 3-SAT wrt. alpha is the key motivating factor for choosing 3-SAT, similar situations could maybe also arise in classic combinatorial problems over random graphs.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the reasoning capabilities of large language models (LLMs) through the perspective of statistical computational complexity. This framework analyzes computational complexity as a random variable influenced by specific order parameters of a given problem. The focus of this investigation is 3-SAT, a problem extensively studied in the AI literature for its phase transition phenomena. The authors demonstrate that state-of-the-art LLMs face significant challenges in solving random instances with up to 10 variables. Not only do LLMs struggle to resolve instances located in the phase-transition region, but they also often fail to address instances in the simpler regions that are either under-constrained or over-constrained. Additionally, the authors propose that an LLM-modulo SAT framework, which integrates an LLM architecture with a SAT solver, presents an alternative for tackling simple commonsense reasoning tasks that can be reframed as 3-SAT problems.

### Strengths
**Novelty:** While recent studies have examined the reasoning limitations of LLMs from a computational perspective, this paper provides new empirical findings through a statistical complexity analysis. One of the most noteworthy observations is the difficulty LLMs face in effectively addressing "simple" constraint satisfaction problems (CSPs). By "simple," I refer to CSP instances that involve no more than 10 variables, which are regarded as toy problems within the constraint programming community. For these instances, it appears that most LLMs do not significantly outperform a random baseline (Left part of Figure 4).

### Weaknesses
 **Positioning:** Although I am convinced that the paper is conveying something new, the related work section could benefit from further elaboration, particularly in discussing the empirical results presented in this paper alongside recent studies that have theoretically and/or empirically explored the reasoning limitations of large language models (LLMs). Notably, Dziri et al. (2023) have experimentally demonstrated that the performance of Transformers on constraint reasoning tasks declines rapidly as the depth of the task increases. Furthermore, Peng et al. (2024) have shown that the satisfiability of Krom, Horn, or affine formulas cannot be determined by multi-layer Transformers unless L = NL. Hence, the new results concerning random 3-SAT instances are, at first glance, not particularly surprising.

**Clarity:** The first four sections are relatively clear, but I found the results in Section 5.1 and the significance of Section 5.2 confusing. In Section 5.1, why do the accuracy results for GPT-4 differ when comparing the left parts of Figure 3 and Figure 4?  I also found the experimental protocol in Section 5.2 somewhat perplexing. As I understand it, a constraint satisfaction problem described in natural language is first translated into a 3-SAT instance by a large language model (LLM) and then processed by a SAT solver. In this case, the “positive” results are not surprising at all, since the LLM is not being used to "reason" about the input problem; it is merely parsing the problem into a CNF expression.

**Contribution:** Based on the comments above, the main contribution of this paper is essentially limited to a statistical analysis of the accuracies of large language models (LLMs) on random instances of 3-SAT. By breaking down the distribution of instances into three typical regions, most LLMs struggle to solve instances in all these regions, even when the number of variables $n$ is small. Notably, we cannot conclusively state that GPT-4 behaves similarly to complete or local SAT algorithms for random 3-SAT; even for very easy instances ($\alpha \rightarrow 0$), its performance in finding a solution hovers around 70%. Therefore, a natural extension of this analysis would be to investigate the behavior of LLMs, particularly GPT-4, on simpler constraint satisfaction problems. This would help clarify their reasoning abilities. To this point, I would suggest examining random Krom instances (2-SAT), random Horn instances (HORN), and the intersection of these propositional classes (2-HORN-SAT).

**Minor comment:** In Section 2.2, nowadays, complete SAT solvers use CDCL instead of DPLL (in its basic form).

### Questions
See above comments.

### Soundness
2

### Presentation
3

### Contribution
2
