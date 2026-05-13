# ICDA: Interactive Causal Discovery through Large Language Model Agents

- Decision: Reject
- Scores: 6, 5, 3, 5, 3

## Abstract
Large language models (\textbf{LLMs}) have emerged as a powerful method for causal discovery. Instead of utilizing numerical observational data, LLMs utilize associated variable \textit{semantic metadata} to predict causal relationships. Simultaneously, LLMs demonstrate impressive abilities to act as black-box optimizers when given an objective $f$ and sequence of trials. We study LLMs at the intersection of these two capabilities by applying LLMs to the task of \textit{interactive causal discovery}: given a budget of $I$ edge interventions over $R$ rounds, minimize the distance between the ground truth causal graph $G^*$ and the predicted graph $\hat{G}_R$ at the end of the $R$-th round. We propose an LLM-based pipeline incorporating two key components: 1) an LLM uncertainty-driven method for edge intervention selection 2) a local graph update strategy utilizing binary feedback from interventions to improve predictions for non-intervened neighboring edges. Experiments on eight different real-world graphs show our approach significantly outperforms a random selection baseline: at times by up to 0.5 absolute F1 score. Further we conduct a rigorous series of ablations dissecting the impact of each component of the pipeline. Finally, to assess the impact of memorization, we apply our interactive causal discovery strategy to a complex, new (as of July 2024) causal graph on protein transcription factors. Overall, our results show LLM driven uncertainy based edge selection with local updates performs strongly and robustly across a diverse set of real-world graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed Interactive Causal Discovery Agent (ICDA), that uses LLMs for causal discovery through an uncertainty-driven edge intervention selection process. The method prioritizes uncertain edges for intervention and utilizes local updates from feedback, achieving strong performance on a range of real-world causal graphs. Extensive experiments validate ICDA’s robustness and adaptability, showing it outperforms zero-shot LLM prompting across diverse graph structures.

### Strengths
- The paper introduces a novel application of LLMs for causal discovery - using LLM defined interventions to refine causal discovery.

- ICDA is evaluated on diverse datasets including a dataset not part of the model pertaining.

- The paper is well-written and easy to follow.

### Weaknesses
 - Lack of comparison with statistical methods.

- There is a lack of comprehensive results across models. I acknowledge the authors have presented results in Figure 6, but comparing different ICDA variants and random agents for smaller models would have been interesting.

- Some of the figures done have confidence bound (last subplot for Fig 6). Am I missing something?

- What does "simplicity" mean on L138?

- Some works suggest that LLMs confidence might be unreliable, I wonder what the intuition on much better results with ICDA is in comparison to random agents?

Minor:

- Figures might benefit from increasing the font size.

- a weird indent on L254

### Questions
- Some of the figures done have confidence bound (last subplot for Fig 6). Am I missing something?

- What does "simplicity" mean on L138?

- Some works suggest that LLMs confidence might be unreliable, I wonder what the intuition on much better results with ICDA is in comparison to random agents?

Minor:

- Figures might benefit from increasing the font size.

- a weird indent on L254

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
3

### Summary
The authors propose a new method for end-to-end interactive causal discovery using LLMs.
The approach comprises two main components intervention selection method based on LLM uncertainty predictions and local update strategy based on newly acquired knowledge. 
The approach is based on a formulation of edge intervention. The method is evaluated on the set of 7 real-world graphs and compared against its ablations. Additional analysis is provided which covers evaluation with different LLM models and evaluation on the graph unseen during LLM training.

### Strengths
1. The paper is cleanly written. 
2. The approach is well motivated by the literature. 
3. The experimental section is extensive.

### Weaknesses
1. The definition of edge intervention feels unrealistic. Could the authors please provide an example of a causal operation that reveals the edge without additional knowledge or assumptions about the graph structure? It seems to me that such data might be extremely costly to obtain and the operation might in some cases be equivalent to revealing the whole graph, thus making the described approach impractical. The authors claim that a perturbation of a variable R and observation of a statistically significant change in the distribution of variable T is sufficient to claim a direct causal relation. However, this ignores the possibility of confounding variables and indirect effects. For example, if R influences variable X, which in turn influences T, perturbing R will affect T, but this does not imply a direct causal link between R and T. The paper needs to clarify how the proposed 'edge intervention' can isolate direct causal effects without additional assumptions or knowledge about the graph structure.
2. The paper lacks a discussion about the limitations of the proposed approach.

### Questions
1. The plots in Figures 2 and 4 are very small and hard to read.
2. In line 312 there seems to be a space missing - “weablate”
3. The citation (Sharma & Kiciman, 2020), in line 147 seems misplaced. What was the authors' intention?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies using LLMs to perform causal discovery in an interactive manner.  The authors propose to incorporate LLMs as an agent to produce initial graphs, and iteratively optimize the updated causal graphs by selecting proper interventions. During the selection of the intervention targets, LLMs are leveraged to provide uncertainty measures for the unknown edge. The authors show that the proposed approach can effectively outperforms simple baselines on eight real-world causal graphs.

### Strengths
(+) This work presents an interesting use of LLMs in causal discovery;

(+) The presentation and organization of this work are clear and easy-to-follow;

(+) Some experiments demonstrate the effectiveness of the proposed approach;

### Weaknesses
(-) The setting may not be realistic, since it is challenging to directly obtain the ground-truth causal edge label in each intervention;

(-) There is no guarantee that LLMs could provide valid results;

(-) Previous baselines on experimental design are neglected;

    The setting may not be realistic:
    - In the proposed setting, line 144, it is assumed that one could directly obtain the ground-truth causal edge label in each intervention, which is not realistic;
    - The setting significantly differs from the standard practice in the literature of experimental design [1,2,3];

    There is no guarantee that LLMs could provide valid results:
    - It is widely shown that LLMs can not provide faithful causal results [4,5], while the proposed framework heavily rely on the results of LLMs;
    - Similarly, the uncertainty provided by LLMs is not warranted;

    Previous baselines on experimental design are neglected, for example, previous works on intervention selection or experimental design [1,2,3].

Minor
- The line numbers of the algorithm are all 0; 
- lots of key steps in the algorithm are not defined;

### Questions
1. The setting may not be realistic:
- In the proposed setting, line 144, it is assumed that one could directly obtain the ground-truth causal edge label in each intervention, which is not realistic;
- The setting significantly differs from the standard practice in the literature of experimental design [1,2,3];

2. There is no guarantee that LLMs could provide valid results:
- It is widely shown that LLMs can not provide faithful causal results [4,5], while the proposed framework heavily rely on the results of LLMs;
- Similarly, the uncertainty provided by LLMs is not warranted;

3. Previous baselines on experimental design are neglected, for example, previous works on intervention selection or experimental design [1,2,3].

Minor
- The line numbers of the algorithm are all 0; 
- lots of key steps in the algorithm are not defined;

**Refereneces**

[1] Learning neural causal models with active interventions.

[2] Trust your $\nabla$: Gradient-based intervention targeting for causal discovery.

[3]  Active learning for optimal intervention design in causal models.

[4] Causal parrots: Large language models may talk causality but are not causal.
 
[5] Discovery of the hidden world with large language models.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper builds on previous literature on using LLMs for causal discovery on one side, and for active black-box function optimization on the other side, to iteratively update a graph using ground-truth edges obtained through interventions.

### Strengths
Originalty : The submissions brings an interesting perspective by making use of the use of the literature on LLMs as optimizers.

Quality : the experiments are extensive and exhaustive, performing multiple ablation studies on the model's properties but also on aspects such as memorization.

Clarity : the paper is mostly clear in my opinion.

Signifiance : the experiments are interesting as they underline the importance of finding a subtle balance wrt local updates, between throwing the whole graph into the prompt and only modifying intervened edges.

### Weaknesses
Originalty/Signifiance/Quality : this point harms the correctness of the claims of the paper and is my main concern : it seems like the iterative updates do not satisfy the framework of LLMs as optimizers. From my understanding of the submission and the references, this frameworks consists in having the LLM decide on next points in the admissible space to query based on former (point, function realization) couples. But here, the next edges to query are done in a pre-determined, algorithmic manner, based on confidences, and the objective (the F1 score) is not used as an objective to optimize and is never parsed to the LLMs. The LLM is simply used on a post-hoc manner *after* having queried edges and read their associated output ground-truth labels.

Clarity : there are a few unclear points or mistakes developed in the questions.

### Questions
- Can you elaborate on :
a) how your algorithm satisfies the LLMs as optimizers framework? ;
b) why using the F1 metric specifically as a loss?,
c) why these specific updates on parents of intervened edges as the choice of local updates?,
d) how exactly the intervention is performed, at least in experiments?

- l.94-95 : *Building on Meek (2013), Chickering (2002) proposes a greedy search algorithm that performs well in practice.* There seems to be a confusion in time here... wrong Google Scholar citation?

- Can you increase the font of Figure 2?

- l.403-404 : *Additionally, we notefFor large enough graphs, putting everything in context is simply not feasbile*. Typo? We note that for?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper applies large language models (LLMs) to causal reasoning. Specifically, the authors prompt LLMs to address two key tasks: (1) selecting which edge to intervene on in the next round, and (2) updating the predicted causal graph. The authors demonstrate that their approach significantly outperforms a random selection baseline across eight different real-world graphs.

### Strengths
(1) Introducing LLMs to study causal discovery is an interesting direction.

(2) The author's writing is clear, making it easy to read and understand.

### Weaknesses
 (1) The experimental setup is quite simple, comparing only three basic methods: random selection, direct LLM, and static confidence selection.

(2) Additionally, the comparison should include the performance of different language models, not just one.

(3) In the main experimental section, it would be better to include a table for quantitative results alongside the graphs.

(4) The experimental setup is overly simplistic, and for a conference like ICLR, the complexity of the method, theoretical analysis, and experimental thoroughness are insufficient.

### Questions
Refer to weakness.

### Soundness
2

### Presentation
3

### Contribution
2
