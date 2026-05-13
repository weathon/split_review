# CBGBench: Fill in the Blank of Protein-Molecule Complex Binding Graph

- Decision: Accept
- Scores: 8, 8, 8, 5, 8

## Abstract
Structure-based drug design (SBDD) aims to generate potential drugs that can bind to a target protein and is greatly expedited by the aid of AI techniques in generative models. However, a lack of systematic understanding persists due to the diverse settings, complex implementation, difficult reproducibility, and task singularity. Firstly, the absence of standardization can lead to unfair comparisons and inconclusive insights. To address this dilemma, we propose CBGBench, a comprehensive benchmark for SBDD, that unifies the task as a generative graph completion, analogous to fill-in-the-blank of the 3D complex binding graph. By categorizing existing methods based on their attributes, CBGBench facilitates a modular and extensible framework that implements various cutting-edge methods. Secondly, a single de novo molecule generation task can hardly reflect their capabilities. To broaden the scope, we adapt these models to a range of tasks essential in drug design, considered sub-tasks within the graph fill-in-the-blank tasks. These tasks include the generative designation of de novo molecules, linkers, fragments, scaffolds, and sidechains, all conditioned on the structures of protein pockets. Our evaluations are conducted with fairness, encompassing comprehensive perspectives on interaction, chemical properties, geometry authenticity, and substructure validity. We further provide deep insights with analysis from empirical studies. Our results indicate that there is potential for further improvements on many tasks, with optimization in network architectures, and effective incorporation of chemical prior knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a benchmark for SBDD, including a unified framework of generative graph completion for multiple tasks in the field and a comprehensive evaluation protocol.

### Strengths
1. The unified code base is a nice contribution to the community and beneficial for future research.
2. The evaluation protocol is comprehensive with a reasonable benchmark setting.
3. The benchmarked methods are representative and state-of-the-art.

### Weaknesses
1. It would be better if the author could discuss the recent trend of training a unified model for small molecules and macromolecules such as proteins and nucleic acids, and its implications on the field of SBDD.

### Questions
1. Why do you choose different GNN architectures for auto-regressive and diffusion-based models?
2. MolCraft seems to be missing from the t-SNE visualization in Figure 8. Also, the distributions of Vina Dock Energy and LBE are not provided. Could you please provide these results?
3. [credit to Associate PC] How might your benchmark and evaluation protocol need to be adapted to assess unified models that can generate both small molecules and macromolecules like proteins?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes CBGBench, a comprehensive benchmark for SBDD tasks, which aims to unify various generative models in a fill-in-the-blank framework for 3D complex binding graphs. It introduces a modular and extensible framework and evaluates multiple state-of-the-art methods across different metrics, including interaction, chemical properties, geometric authenticity, and substructure validity. The paper also introduces four sub-tasks: linker, fragment, side-chain, and scaffold design, to provide insights into lead optimization applications.

### Strengths
The paper fills a notable gap in the SBDD domain by providing a well-structured and unified benchmarking framework. The comprehensive evaluation protocol addresses the diverse nature of generative tasks.

The study uses extensive metrics to evaluate models, including metrics like Ligand Binding Efficiency (LBE) to address the size bias in generated molecules.

Application to real pharmaceutical targets like ADRB1 and DRD3 demonstrates the practical potential of the benchmark and supports the generalizability of the findings.

Overall it's a really well executed paper that focuses on an particular case of generative models, which is drug design, but deserved an acceptance to the main conference due to the relevance of the task.

### Weaknesses
Further testing on more diverse real world systems should be done. Exploring how this models behave in systems like KRAS12 for instance where the main goal is growing into subpockets, would enrich this study.

### Questions
Include more systems that showcase corner cases for a benchmark that are common in real scenarios. i.e KRAS12, BRD4

The comments were satisfactorily addressed.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CBGBench, addressing the gap where the absence of standardization can lead to unfair comparisons and inconclusive insights. On one hand, this paper incorporates recent state-of-the-art studies into a unified framework for fair comparisons; on the other, it extends de novo SBDD tasks to include lead optimization and other related tasks. The paper conducts extensive experiments on these tasks and provides the corresponding code.

### Strengths
S1. This paper has evaluated almost all the prevailing SBDD methods in generative models in AI conference. 
S2. It adapt some of the models to a range of tasks essential in drug design, considered sub-tasks within the graph fill-in-the-blank tasks.
S3. It establish a training, sampling and evaluation codebase, which is comprehensive and effective affter my testing.
S4. The benchmark evaluates all the models for the two real-world target proteins, as a solid case study.

### Weaknesses
W1. Doubts of classification: In Line 165, it states that MolCraft using BFN as the variant of the diffusion models. However, I have two questions, Firstly, it appears that “one-shot model” in the paper refers to diffusion-based models. Given this, is it reasonable to classify BFN as a diffusion model? MolCraft generates in parameter space, while diffusion generates in data space, which I believe is a distinction. Is the authors’ classification reasonable in this regard?

W2. Doubts of evaluation metrics:  The article compares the clash ratio between protein and molecule interactions, denoted as Ratio_cca . Additionally, it defines the internal clash ratio within molecules, denoted as  Ratio_cm . Regarding the internal clash within molecules, since there are bonds connecting atoms, the defined “van der Waals radii overlap by ≥0.4Å” does not hold. For example, if this definition were applied to a benzene ring, the clash ratio would be 1.0, which fails to reflect the actual structural integrity of the molecule. Therefore, I believe this metric is unreasonable. 

Minor: 
Additionally, the article lacks citations for recent work related to SBDD and molecular generation, such as [1] [2]. I suggest that the authors include these references to enhance the completeness of the article.

[1] Zaixi Zhang, Mengdi Wang, Qi Lium. FlexSBDD: Structure-Based Drug Design with Flexible Protein Modeling
[2] Odin Zhang，et al. Deep Lead Optimization: Leveraging Generative AI for Structural Modification

### Questions
See Weakeness. The W1 and W2 are my main concern, and if a satisfactory response can be provided to the above issues, I will consider increasing the score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an extended benchmark protocol for SBDD methods, and does a large comparison of existing literature, and draws some insights from the results.

-----

Post-response update. My initial confusions have been adressed in the response, as well as issues in motivation. This is a useful contribution to SBDD's, with weaknesses wrt incrementality, presentation and experimental insights. I'm increasing my score to borderline, and I'm still leaning on rejection while I wouldn't mind acceptance.

### Strengths
- The paper does a comprehensive benchmark, with lots of interesting results.
- The authors contribute a unified codebase, which could be very useful for future research.

### Weaknesses
- The motivation of the work is weak. I’m not sure why we need all of this stuff, or what questions the paper answers. The paper seems to establish an extended benchmark protocol that adds few extra evaluations to standard benchmarks. This could be useful, but I found the new additions to be a bit hand-wavy. The paper also proposes “unified” tasks and notation, but why? These tasks and notation is already common.
- The novel contributions of the work seem limited. The data and tasks seem to be from earlier works, and the benchmarks are added with just few extra evaluations, which also all seem to already exist. The main contribution is collecting all of this into one place. The performance comparison is a good contribution, but similar comparisons are done in every paper. The proposed new “unified” notation or task framing seems all well known. The main new contribution is probably the unified codebase, which can be very useful. The paper draws a bunch of conclusions from the results, which are interesting, but it’s unclear how novel they are.
- As a benchmark paper the presentation of the results is limited: there are too many decimals, no standard deviations, and there are lots of massive tables of “raw” performance values, which are not digested into transferable insights. The analysis is superficial, and there are no ablations or attempts to explain how or why the different methods perform differently. 
- As a survey paper I didn't find this paper particularly good at summarising or organising the domain in terms of methods, data or metrics. Use of math is inconsistent.

### Questions
- It would be useful to extend the method table by also including which tasks they support, and their architectures and losses
- Training losses should be discussed
- The paper first describes the main de novo task very superficially, then it describes the subtasks more in-depth, then it goes back to describing the de novo task more in detail, and finally goes back to subtasks. It would have been much clearer to separate the main/sub tasks into different parts of the paper.
- The task description is missing the objectives/metrics. Overall I didn’t really understand the role of the four subtasks. These are very specific, and surely each method needs to have custom support for them. Which ones do? Do we expect new methods to support these 4 tasks? Isn’t it enough that a method is good at the “basic” de novo generation? I’m a bit confused why we care about these at all, or what is their significance? It’s also unclear how they relate to the probabilistic model or ML modelling. Are these some kind of conditionals?
- It’s unclear if the 4 tasks in table 2 have something to do with the main task. That is, do they share data in some sense? Are the 4 tasks more fine-grained versions of the de-novo data?
- I’m a bit confused what’s the point of the “unified” probabilistic model notation. It seems that this is used nowhere in the paper after it’s introduction.
- Why would you look at the MAE between two distributions? This doesn’t seem sensible. The distribution sizes and domains and types are mostly undefined [please use precise math]
- What does it mean to measure “atom types” of functional groups? I don’t understand. I though that you compared just some distributions of 25 groups, which should give you a probability vector of length 25 to be compared. The at/rt/fg should have no role here. [It would help so much to define the stuff in precise math so that I wouldn’t have to guess.]
- I fail to see where the accuracy of the de novo generation is described. I thought the task is to predict the correct ligand for a known protein (assuming there is only one correct ligand). Surely you want to measure how often you get this right. The paper also talks about probabilistic model of p(M|P). Where is this density evaluated: shouldn’t we see some logp values in the results?
- Or is the task to just generate some ligands (irrespective if it was the correct one), as long as they have good binding and properties, or come from some distribution? If the task really is generative, then one expects to use learning target of maximizing the model likelihood of the observed data (both training and test folds). I don’t see this in the paper either. The learning problem needs to be precise.
- Overall it seems that some metrics in the paper are about checking that the summary statistics of $p(ligand)$ or $p(ligand|protein)$ match the true distributions, and some are about making sure some $fitness(ligand,protein)$ is high. This is not formalised well, and it leads to the metrics and learning setting being vague and hand-wavy.  
- I fail to see the motivation for the different Vina scores. If Vina is pathological, then why would we still use it? I don’t see how IMP or MPBG helps either if they are based on Vina. I don’t see convincing arguments why the LBE fixes the Vina pathology: the table 11 has values all of the place. I think here less would be more, and it would be much better to just have one good metric for binding than lots of binding metrics of varying quality. 
- I did not understand the PLIP stuff.
- Overall the metrics are difficult to interpret. I don’t really know what the numbers mean. Is 0.4382 MAE good or bad? Is a 0.2345 JSD high or low? Is Vina -3.75 good or bad? Is IMP 22 good? I have no idea. It would be insightful to visualise the distributions, or use some human-understandable metrics. For instance, you could use distribution overlap percentage or something else.
- It would have been useful to show some example generations, and their corresponding metrics.
- Using 5M iterates in each method seems unfair. Different methods train in different ways. I think you need to analyse the discrepancy between your results and the published results to clarify this.
- It seems that you change some methods architectures for no reason. This is not fair and will nullify the corresponding results. You can’t claim to benchmark method X if you change the method X from the publication.
- It’s unclear if you reimplement the methods in your codebase, or just collect published codebases in one place. Can you clarify?
- “We generate 100 molecules per pocket in test”. How do you do this? Why do you do this? Didn’t we have test data that tells us this? Now there are 10000 test molecules, while table 2 says that there are only 100. The learning setting is confusing, and using math to describe things would help. It seems that the entire setting in this paper is some kind of $D[p_gen || p_obs]$, which is not properly formalised.
- “We show the interaction analysis and chemical property in the main context and omit the interaction pattern analysis since maintaining the patterns is not necessary for lead optimization.” I don’t understand this. How do you use “chemical property” as context? How do you use “analysis” as context? What is "context"?
- I don’t understand what you do in the subtask training. Surely a method can’t be just applied in eg. linker generation if it wasn’t designed to do it? Are all 6 methods ones that support it, or do you somehow kludge this support to them? I’m really confused what do you train for extra 1M steps. What are even the loss functions? This is all super vague.
- The results of subtasks are all over the place. I’m not sure what can you conclude from this.
- Using ECFP to compare molecules in sec 5.3. is a very weak approach, and running it through tsne2d makes it even worse. This analysis has little to no value.
- The setting in 5.3. is weak. Thera are only 100 random controls (why not way more, like a million?). It’s unclear how many molecules you sample, but this should be a large number.
- Sec 5 concludes that the evaluation protocols are very consistent with real-world behavior. By far the best method in sec 5 is the DiffSBDD, which has by far best LBE, and ok Vina’s (Vina is pathological, so we should look at LBE anyways). But in Table 7 we see DiffSBDD being ranked 10/12, ie. one of the worst methods. It’s pretty clear that the real-world performance and de novo benchmark performance is not consistent.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new benchmark for generative models in structure-based drug design. Recently, many machine learning models have been proposed to help solve the problem of designing compounds that can interact with their protein targets. However, the comparison of these methods is difficult due to the lack of standards and relevant benchmarks. CBGBench is a benchmark that aims at standardizing model comparison and proposing evaluation metrics that can be used to assess the performance of generative models. Additionally, the benchmark contains tasks that can be used to evaluate models' capabilities of fragment linking, scaffold hopping, fragment growing, and side chain generation. Several recent generative models were compared using the proposed benchmark, and conclusions were drawn from these experiments. Moreover, a case study was conducted to demonstrate the quality of compounds generated by these methods for two selected GPCR targets.

### Strengths
Originality:
- A new benchmark is proposed for comparing the performance of recently developed SBDD methods.
- This benchmark also includes additional tasks like fragment linking or scaffold hopping, for which do not exist any standardized benchmarks.
- A taxonomy of SBDD generative models is proposed.

Quality:
- The benchmark covers a wide range of generative models, including autoregressive and one-shot generative models.
- Both evaluation methods and scoring network architectures are standardized.

Clarity:
- The benchmark is clearly defined, and the diagrams in Figures 2 and 3 explain different tasks and model types.
- The evaluation metrics are explained in an easy-to-follow way.

Significance:
- The proposed benchmark should accelerate research on new generative models that generate molecules binding to a given protein.
- The benchmarking code is attached to this submission, making it easier to test new models in the future.

### Weaknesses
Originality:
- This work does not discuss other benchmarks for generative methods. In particular, Zheng et al. [1] have recently introduced an SBDD benchmark for generative models.

[1] Zheng, Kangyu, et al. "Structure-based Drug Design Benchmark: Do 3D Methods Really Dominate?." arXiv preprint arXiv:2406.03403 (2024).

Quality:
- The requirement that "each connecting fragment must consist of more than five atoms" seems arbitrary. Why are models that occasionally generate fewer atoms considered insufficient?
- The benchmark could propose a method of computing confidence intervals, e.g. by sampling the generated molecules. It would facilitate the judgment of whether one of the tested models is significantly better than the others.

Clarity:
- "Real-world targets" may be a confusing name for the structures used in the case study. The protein structures in the CrossDocked2020 dataset were also real-world targets, which might confuse some readers. Maybe it would be better to call the structures in the case study as selected targets.
- Additionally, I recommend rephrasing statements like "the established evaluation protocols exhibit strong consistency and generalizability on real-world target data." The real-world target data could be understood as binding data from laboratory experiments, but docking experiments usually do not correlate with such experimental data.
- The text in Figures 4 and 5 may be too small.

Minor comments:
- A typo in line 68: "Vina enery"
- A typo in line 475 "the neurotrans-625 mitter"

### Questions
1. What is the difference between fragment growing and side chain decoration on the implementation level? The text mentions ligand decomposition for the fragment growing task, but the detailed procedure of the decomposition is not explained. In Figure 3, how is the scaffold selected in the case of side chain decoration?
2. Some of the employed evaluation metrics compare the generated distribution of molecules to a known distribution of molecules. Would this approach not penalize methods that generate molecules with novel scaffolds? Also in the t-SNE plot (Figure 4) that compares the set of generated molecules to the actives, the compounds generated by a model can be significantly different from the known actives but still active. A good example of this behavior would be genetic algorithms that optimize docking scores. These methods are not trained on any data, so they can easily learn to produce compounds that have a unique structure and dock well to the target protein.

### Soundness
3

### Presentation
3

### Contribution
3
