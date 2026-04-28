# MAGNet: Motif-Agnostic Generation of Molecules from Scaffolds

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 8, 5

## Abstract
Recent advances in machine learning for molecules exhibit great potential for facilitating drug discovery from \emph{in silico} predictions.
Most models for molecule generation rely on the decomposition of molecules into frequently occurring substructures (motifs), from which they generate novel compounds. 
While motif representations greatly aid in learning molecular distributions, such methods struggle to represent substructures beyond their known motif set. 
To alleviate this issue and increase flexibility across datasets, we propose \modelname, a graph-based model that generates abstract shapes before allocating atom and bond types. 
To this end, we introduce a novel factorisation of the molecules' data distribution that accounts for the molecules' global context and facilitates learning adequate assignments of atoms and bonds onto shapes. Despite the added complexity of shape abstractions, \modelname\ outperforms most other graph-based approaches on standard benchmarks. Importantly, we demonstrate that \modelname's improved expressivity leads to molecules with more topologically distinct structures and, at the same time, diverse atom and bond assignments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new way to address chunk-based molecule generation. Instead of using fully specified molecular subgraphs (motifs) similarly to prior work, the authors instead abstract out motifs to their connectivity skeletons, which allows for a smaller vocabulary to cover a wider range of possible motif realizations. The authors then show a factorization of the generative procedure that first builds the scaffold by assembling these motif skeletons and then gradually fills in the atom features. The approach is verified on standard generation and optimization benchmarks, showing decent performance.

### Strengths
(S1): The authors address an important problem of molecule generation, and identify a reasonable gap in the capabilities of prior models that they then try to address. The proposed approach is motivated clearly. 

 

(S2): The paper is generally well-written. The experiments are conducted across various setups that are common/relevant in this domain. While the empirical performance isn't across-the-board amazing, MAGNet seems to be a generally capable model with good performance overall, while improving on top of previous models in some settings, as well as enabling new capabilities (e.g. more ways to condition the generation on partial information).

### Weaknesses
 (W1): The authors argue the most direct comparison is to other OS models, and focus on that angle. Setting aside the fact that MAGNet is not purely one-shot as the scaffold multiset `S` is decoded sequentially and autoregressively, even if we agree MAGNet is OS, is there any inherent value that comes from being an OS model? One thing that comes to mind would be faster inference, as stepwise generation models can be expensive due to repeatedly encoding the current partial graph. So, is MAGNet more efficient than sequential decoding models, e.g. MoLeR? It would be useful to see a more detailed analysis of the computational cost, including memory usage and wall-clock time, especially when compared to sequential models. The current analysis focuses on the number of parameters, which is not necessarily indicative of the actual runtime performance.

 (W2): More interesting conditioning settings depicted in Figure 5 could be explained in more detail. The partial molecule induces a partial scaffold multiset `S`; do you then use this partial multiset and continue generating to get a full multiset, then connect the scaffolds while forcing those of the connections that are implied from the conditioning? I assume extending the multiset `S` with further scaffolds cannot directly take into account the fact that some of the scaffold connections (or scaffold instantiations into specific motifs) are already known from the conditioning, because during training the scaffold multiset extension subnetwork assumes only a multiset of generic scaffolds is known. Could this be an issue causing the model to add scaffolds that don't fit well with the partial molecule? For example, if the partial molecule has a specific ring system, is the model capable of respecting this constraint, or could it potentially generate a molecule with a different ring system due to the lack of explicit conditioning on the partial molecule's connectivity during scaffold generation?

=== Nitpicks ===

Below I list nitpicks (e.g. typos, grammar errors), which did not have a significant impact on my review score, but it would be good to fix those to improve the paper further.

- Line 147: Denoting the join node as `j` could be an index clash given that the scaffolds being considered are denoted as `i` and `j` earlier in the sentence.

- Line 155: "factories" -> "factorize"

- Line 309: missing space

=== Update 26/11 ===

After the author rebuttal I decided to raise my score from 6 (borderline accept) to 8 (accept).

### Questions
See the "Weaknesses" section above for specific questions.

If my questions/concerns are addressed, I would consider raising my score.

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
The paper presents MAGnet, a generative model for molecules. MAGnet is based on scaffolds (an abstraction of molecular fragments without atom and bond information, just the graph structure), which are introduced to factorize of the molecule distribution. MAGnet is a VAE-like architecture which generates new molecules by first predicting a scaffold set and its connectivity from latent space, then by predicting the atom and bond types for each scaffold, and finally by adding leaf nodes. Experiments show good performances in comparison with several baselines, on standard benchmarks such as GuacaMol and MOSES.

### Strengths
- using scaffolds instead of motifs qualifies as an innovative proposal, which could be of value to the community
- experimental evaluation is extensive in both depth (many baselines) and width (two benchmarks)

### Weaknesses
throughout the paper, MAGnet is considered a one-shot (OS) molecule generator, when in fact it is auto-regressive (AR). Appendix B.2 states that the set of scaffolds is generated auto-regressively, so I cannot understand how it could be considered one-shot. According to the definition by Zhu et al. (2022):


    Sequential generation refers to generating graphs in a set of consecutive steps, usually done nodes by nodes and edges by edges. One-shot generation, instead, refers to generating the node feature and edge feature matrices in one single step.

This is very different from what it is stated in Section 2 of the MAGnet paper:

    Zhu et al. (2022) categorise the generation process further into sequential methods, building molecules per fragment while conditioning on a partial molecule.

to justify the fact that MAGnet is OS. According to the same paper that is cited, MAGnet belongs to the AR category. If MAGnet is AR, then most claims made in the paper need to be toned down or changed because it falls in the same category as MoLeR, which has usually comparable or better performances than MAGnet. For example, the claim "MAGnet is the best OS generator" no longer makes sense. The core issue is that the paper uses the term 'one-shot' to describe a process where the scaffold connectivity is generated in a single step, but the scaffold *set* itself is generated autoregressively, which is a crucial distinction. This mischaracterization undermines the novelty claims, as it positions MAGnet as a one-shot method when it shares fundamental characteristics with autoregressive models. The paper's framing suggests that MAGnet's performance is superior to other one-shot methods, but this comparison is misleading if MAGnet is actually an autoregressive model. This incorrect classification impacts the interpretation of the experimental results, especially when compared to other autoregressive methods like MoLeR. The paper needs to clarify the distinction between generating the scaffold connectivity in one step and generating the scaffold set autoregressively, and how this impacts the overall classification of the model.

### Questions
I'll be honest here. I really liked this paper and I was going to recommend clear acceptance until I understood that MAGnet was an AR model "disguised" as an OS model. From that point onward, I couldn't shake the feeling that it was framed as OS only because, if put in the AR category, the results would become not so impressive (although still good). I really hope this was an unintentional mistake or misinterpretation by the authors. That's a shame in my opinion, since I believe the proposal is original and the evaluation was very thorough, the technical side of this paper is almost flawless. 

I will be recommending rejection of this paper for the moment, because in this form too many claims made in this paper stem from an incorrect premise. However, I am willing to hear from the authors why they consider MAGnet one-shot instead of sequential and will re-evaluate whether I could reconsider my judgment after the rebuttal phase.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors aim to address a fundamental limitation of fragment-based molecular generators. The vocabulary of such models is defined as the union of common molecular fragments, obtained from datasets of known molecules, and individual atoms, which can be used to re-generate motifs that would not be listed under the available fragments. The authors argue that this choice of vocabulary creates an inherent tradeoff in the expressivity of the model. On the on hand, including more fragments quickly increases the vocabulary of the model, with the number of motif variation increasing exponentially with their size. On the other hand, learning to model missing fragments from individual atoms is a challenging task requiring even more training data and often leading to unrealistic molecular motifs. 

As a solution, the authors propose a coarse-to-fine-grained molecular generation paradigm centred around molecular scaffolds, rather than fragments, as the basic building block of the model's vocabulary. A single scaffold implicitly captures many similar fragments, allowing for a relatively small vocabulary size while retaining expressivity. The proposed model, MAGNet, a VAE-based molecular generator, operates on this multi-level factorisation paradigm, by first sampling scaffolds and only then specifying the atomic composition of the scaffolds, their joints and the leaf nodes as a successive step. They evaluate this approach on several benchmarks against a variety of baselines and show that the proposed method, with its more expressive vocabulary, can reliably generate complex molecular motifs, in addition to allow for latent code optimisation and interpolation.

### Strengths
In general, I found the paper interesting and very well written. It clearly identifies a limitation of current fragment-based molecular generators in terms of expressivity, and present a well motivated solution based on a novel factorisation paradigm. I believe this is a good paper which brings significant contributions to fragment-based molecular generation approaches and for this reason I recommend that the paper should be accepted. I suggested some clarifications (see below) which I think would increase the clarity of the paper and complement the discussion on the limitations of the method and the general positioning of fragment-based and one-shot graph molecular generators.

A few specific notes:
1. The Related Work section is exhaustive.
2. The proposed method is clearly introduced and detailed. In particular Figures 2 and 6 effectively convey the hierarchy supporting this paradigm.
3. The experimental section is well structured and the authors compare to a large array of prior work and using several public datasets. The results effectively support the main claims made in the paper. In particular, the results presented in Figure 3, Figure 4 are compelling.

### Weaknesses
1. One of the main limitation of fragment-based methods is the absence of synthesizability considerations in the framework design. This significantly limits the applicability of such methods since, to be tested in physical and biological assays, the proposed molecules either require individual and expansive custom synthesis plans or have to be replaced by available analogs, thus drastically under-utilizing the expressivity of the model. It would be interesting to further discuss the limitations of the proposed method w.r.t. synthesizability in the manuscript. Specifically, the discussion should address the fact that while the scaffold-based approach may generate novel structures, these structures might be even more challenging to synthesize than those generated by fragment-based methods, which at least have a chance of being composed of known, synthesizable fragments. A more detailed analysis of the chemical feasibility of the generated molecules is needed.
2. On line 371: "We do not report Novelty and Uniqueness, as almost all evaluated models achieve 100% on these metrics." if this claim is made, then the numbers should be presented (at least in Appendix). Same for the mention right after: "For the baselines DiGress, SM-LSTM, and CharVAE, which are not able to achieve 100% Validity, we sample until we obtain 10^4 valid molecules", it could be informative to include these numbers in appendix (validity rate for each method). The absence of these metrics makes it difficult to fully assess the performance of the proposed method against the baselines.
3. It would be useful to specify a bit more clearly how benchmarking on Guacamol is executed (lines 301-304 and 309-311). Is the model trained on ZINC and then evaluated on some reference set defined by Guacamol (Chembl)? Or is the model trained on Chembl molecules and compared to a test set also defined in Guacamol? While the provided references are useful, the description of the experiments should be standalone in the paper. The current description lacks sufficient detail to fully reproduce the experimental setup.
4. In the goal-directed evaluations, it would be interesting to compare MAGNet with methods specifically aimed at goal-directed molecular design such as RL and GFlownet based methods. The current comparison only focuses on fragment-based methods, which does not fully contextualize the performance of MAGNet in the broader landscape of molecular design approaches.

### Questions
1. My understanding of the experiments presented in Figure 1-a, Figure 3 and Figure 9 carried out (Section 5.1) is that the fragment-based approaches fail to reconstruct complex motifs that are absent from their fragment vocabulary by using atom-based tokens only. In contrast, MAGNet contained these structures in its scaffold vocabulary. Why haven't both methods used the same dataset to construct their fragment/scaffold vocabularies, without limiting fragment-based methods to only the top-K fragments (i.e. including all fragments). In this case, the modeling task from the fragment-based methods using a vast vocabulary of fragments would be more difficult, but the method wouldn't lack these important fragments such as big rings, preventing them from reconstructing specific molecules. Have experiments on the baselines been carried out by varying the value of "k" in the top-k fragment-based vocabularies to see how vocabulary size trades-off with learning complexity? It seems to me that this might be a point where a more appropriate tuning of the baseline's hyperparameters would make a difference. And if the main advantage of the proposed factorisation is that it removes the need for such tuning when constructing the fragment vocabulary, it would be interesting to discuss these considerations in the paper.

### Soundness
4

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
4

### Summary
This paper addresses a critical limitation in substructure-based molecular generative models: the inability to capture the structural diversity in molecular space due to missing complex structures from the motif vocabulary. The authors propose a novel approach that employs a structural scaffold vocabulary, leaving atom and bond types to be predicted by the model. This approach is intended to enrich structural diversity, with specific metrics introduced to highlight the advantages of the proposed method.

### Strengths
1. The paper tackles a significant issue in 2D molecular generation, and Figure 1a provides an illustrative example that emphasizes the limitations of current motif-based methods in generating novel molecular structures. This emphasis on structural diversity is both timely and impactful for the field.


2. Experimental results demonstrate an increase in generated structural diversity.

### Weaknesses
1. **Limitations in Generating Novel Molecular Structures**

1.1 A primary concern is whether the proposed solution truly resolves the problem of generating novel molecular structures. As highlighted in Figure 1a, the generation of new substructures—particularly complex fused ring systems—appears challenging. Both the original motif approach and the scaffold motif proposed in this work seem constrained in their ability to construct unseen complex fused rings because they are hard to piece together using substructures in the vocabulary. Specifically, while the method aims to improve structural diversity, the core issue of generating truly novel ring systems, beyond simple combinations of known scaffolds, remains unaddressed. The method seems limited to generating molecules within the structural space defined by the scaffold vocabulary, which may not be sufficient for discovering molecules with completely new ring arrangements.

1.2 Furthermore, while the scaffold motif approach can potentially reduce vocabulary size, it still requires additional specification of bonds and atom types on rings, which might affect the validity of atom valence of the generated molecules. The process of predicting atom and bond types on a pre-defined scaffold introduces additional complexity and potential for generating invalid structures, especially when dealing with complex scaffolds where the valence constraints are more intricate. This two-step approach, while aiming for diversity, might inadvertently increase the likelihood of generating molecules that violate basic chemical rules.

Thus, while the problem raised is compelling, the method appears to partially address, rather than fully resolve, this issue.

2. **Writing**

2.1 Overlap in Sections 3 and 4: Sections 3 and 4 present overlapping content, which could benefit from a clearer delineation. Specifically, Section 4 should focus more on detailing the network structures (architecture) within each module, and provide an illustration of the model structure. The high-level probability descriptions, already covered in Section 3, could be streamlined here. The current structure makes it difficult to distinguish between the theoretical framework and the specific implementation details of the model. A clearer separation would enhance the readability and understanding of the proposed method.

2.2 Figure Captions: In Figure 3, the captions for panels (b) and (c) appear reversed.

2.3 References: The authors should thoroughly review the reference list for consistency. It is full of preprint references.  Accepted papers should reference their final publication locations rather than preprints (e.g. MiCaM and ShapeMol, etc). Please also check with repeated links and unusual endings with paper abbreviations (e.g. G-SchNet, JODO, etc.).

3. **Experimental Results**

While structural diversity has been enhanced, some important metrics, such as FCD and SA, appear to drop. Additionally, there is no mention of the validity rate of generated molecules in the table 1.

### Questions
1. 
Could the authors provide the **validity** of generated molecules? Are there specific metrics used to ensure that generated molecules are fully **connected**, given that some examples (such as in the bottom row of Figure 11) suggest molecules with broken structures?

2. 
A comparison with baseline methods in terms of **generation speed** would add valuable context for practical deployment. 

3. 
Could the authors clarify the **vocabulary size** difference between your approach and baseline models?

### Soundness
2

### Presentation
2

### Contribution
2
