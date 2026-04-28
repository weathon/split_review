# ProteiNexus: Illuminating Protein Pathways through Structural Pre-training

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Protein representation learning has emerged as a powerful tool for various biological tasks. Language models derived from protein sequences represent the predominant trend in many current approaches. However, recent advances reveal that protein sequences alone cannot fully encapsulate the abundant information contained within protein structures, critical for understanding protein function and aiding innovative protein design. In this study, we present ProteiNexus, an innovative approach, effectively integrating protein structure learning with numerous downstream tasks. We propose a structural encoding mechanism adept at capturing fine-grained distance details and spatial positioning. By implementing a robust pre-training strategy and fine-tuning with lightweight decoders designed for specific downstream tasks, our model exhibits outstanding performance, establishing new benchmarks across a range of tasks. The code and models could be found at github repos.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new pretraining approach for learning protein representations, which integrates both structural information and information about downstream tasks. The paper compares their approach to the state-of-the-art on a range of different tasks and report very favourable results.

### Strengths
The paper presents a potential solution to a highly relevant problem. The authors have compiled a very comprehensive list of relevant downstream tasks, and thereby make a good the case for a generally useful pretrained model. The reported results are highly competitive. If they hold, the method could thus have a real impact for practitioners in the application domain.

### Weaknesses
First of all, I have a slight concern about how well this manuscript fits within the scope of the ICLR venue. Although the title and the introduction point towards a new method, the effective focus of the paper seems to be on benchmarking their method, rather than on the method itself. It seems odd to me that most of the description of the model itself has been moved to the appendix, despite the fact that this would presumably be the most interesting part for most of the ICLR community. For instance, the procedure for fine-tuning on downstream tasks is described in a single sentence in the main text - although it is quite central to their approach.

Secondly, despite the fact that the focus is on the benchmarking, there are details missing about the experiments that makes it difficult for me to judge how much faith can be placed in the reported results. For several experiments (see details below), it is unclear how data was split between training, validation and test - and whether this was done in the same way for all methods that were compared in the result tables. Of particular importance, I did not find it clear whether there was overlap in the pre-training data and the data used for downstream testing. In appendix E.3, the authors have a few reflections on this topic, and seem to show a substantial drop in performance for the protein design task when removing part of the pretraining set. This seems like a red flag to me, which should be investigated more thoroughly - and not only for the protein design task.

Finally, the paper itself does not provide a good explanation for why their approach outperforms prior methods. For the community, it would be useful to know if this relies primarily on the structural signal or the fine-tuning on downstream tasks. These questions are potentially partially addressed by the ablation study in appendix E, but the ablation results are never discussed in the main paper. Also, as far as I could see, the effect on fine-tuning on downstream tasks is not ablated - i.e. the difference between fine-tuning the entire pre-trained model or training a downstream model on a fixed pre-trained model.



### Questions
Page 2. *"Predominantly, graph-based representations struggle to preserve ﬁne-grained atom information effectively. Moreover, they tend to accentuate interactions among neighboring residues while often disregarding the inﬂuence of longrange interactions."*
Could you provide a reference to back up this statement?

Page 3. *"Additionally, there are methods that transfer protein structures into distance matrices and attempt to denoise noisy distance matrices while simultaneously predicting the types of corresponding residue types. These approaches undergo pre-training on large-scale datasets to improve the quality and generalizability of the representations."*
Could you provide citations for these methods?

Page 4. *"Lastly, we partition the continuous coordinates into bins of equal width and transform each bin into an embedding"*
Could you describe the motivation for this choice to discretize?

Page 4. *"the "distance tokenizer" method"*
As far as I can see, this method has not been introduced in the paper. Could you elaborate?

Page 4. *"Speciﬁcally, we employ a one-hot encoding scheme to represent the relative distance between position i and position j in the sequence"*
Why use a one-hot encoding to represent a distance? - doesn’t this mean that there is no distinction between bins that are similar in distance and bins that are far apart?

Page 4. *"To better capture the global features and interactions of protein structures, we have opted for the transformer architecture as the backbone of our network. This decision is grounded in the inherent self-attention mechanism of the transformer, which enables computations across the entire protein sequence."*
I don’t understand the distinction you make here. If the graph attention is not capturing enough of the interactions you wish for, can’t you then change the graph to include more interactions? In particular, as far as I can see, graph attention in a fully connected graph would be identical to the attention in a transformer. From that perspective, isn't your approach just a special case of graph attention?

Page 5. *"masked residues"*
"What does “masked residue” mean exactly. Are you masking the identity, or also the atom coordinates?"

Page 5. *"encourage the model to recover authentic atom-level coordinate from noise-induced residue-level pair representations."*
Could you be more precise? How is this "encouraged"?

Page 5. *"Our training dataset includes decoys derived from 7992 unique native protein structures, obtained from DeepAccNet. In the end, we have a collection of 39057 structures in our training dataset, with a fraction representing native structures."*
Since it is central to the data generation process, you should explain in detail what DeepAccNet is, and why it makes sense to use decoys generated by this method as training data. EDIT: I see that you introduce DeepAccNet in the next paragraph, so part of the problem could be resolved by moving that introduction up here. But even when doing so, it is still not clear how the decoys are generated by this method, since it as far as I can see normally produces LDDT scores as output.

Page 5. *"our test set is meticulously curated. It includes targets with experimentally resolved structures from CASP14 and CASP15, paired with their corresponding predicted structures. To ensure diversity and representativeness, we perform a redundancy reduction process on the test set, limiting sequence identity between targets to within 70%."*
Do you also ensure that there is no overlap (high sequence similarity) between the test set and the 7992 structures in your training set? 
The choice of homology reduction to 70% seems rather high to me (we generally use values at 30% to avoid leakage). Why was this choice made? I guess you could verify whether this is a problem by plotting the performance as a function of homology to the nearest protein in the training set.

Page 5. *"We validate our pre-training model on ﬁve datasets"*
Does this mean that you in this case do not train a downstream model, but directly use the frequencies of the pretrained model to obtain and estimate of the binding affinity. This should be clarified. If you do use a downstream model, you should clarify how the splits for training/test were constructed (and whether they overlap with the pretraining set). In particular, it is important to establish whether the methods in Table 2 are actually comparable (i.e whether we believe that none of them have been trained on the current test set).

Table 3
Were these other methods run with exactly the same train/test splits as you run your method. In other words, are the results comparable?

Page 7. *"LSTM (Rao et al., 2019), mLSTM (Alley et al., 2019) and CNN Shanehsazzadeh et al. (2020)."*
It us a bit odd that you use architecture names to refer to specific trained models. It would be clearer if you for instance referred to the first as TAPE-LSTM, and the second as the UniRep model.

Page 7. *"ESM-1b"*
The collection of baseline methods was a bit confusing. For instance, you mention language models like ESM-1b and ProtBert-BFD. How are these employed for fold and enzyme-catalyzed reaction classification? Do you somehow use them in an unsupervised way, or do you put a classification layer on top. If so, it would be clearer if you referred to them by a different name than the language model on which they are based.

Table 4. 
Again, it is unclear if these methods has been trained and tested on exactly the same datasets - in particular since some of the results are copied from other papers. Please clarify.



### Minor comments:

Page 1. "For instance antibodies (such as SARS-CoV2)"
Rephrase. SARS-CoV2 is not an antibody.

Page 1. *"in protein sequences (Consortium, 2019)"*
Change reference to reflect which consortium

Page 1. *"triumph in various tasks including...protein structure prediction (Rao et al., 2020;"*
This paper is about contact prediction, not directly about protein structure prediction.

Table 3. Caption. The title currently says *"Results of classification"*. Would be helpful if you could specify the experiment in the title.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel pretraining approach for protein representation learning that integrates sequential and structural information. The structural encoding mechanism enables the encoder to learn protein distance information and spatial relative positions of residues, overcoming the inherent drawbacks of ignoring long-range interactions of graph-based representations. As a result, the authors present the model ProteiNexus pretrained by a hybrid masking strategy and mixed-noise strategy to comprehensively capture the structural information. The model is fine-tuned with lightweight task-specific decoders, culminating in exemplary performance across a range of downstream tasks, especially in the understanding of protein complexes.

### Strengths
Originality: The paper proposes a novel pretraining strategy which effectively integrates the sequential and structural encoding for the representation learning of proteins. Therefore, the paper uniquely contributes to the field by implementing a simple, yet potent, architecture to capture structural information comprehensively.

Quality: The paper carefully designs the experiments to support the idea. In particular, the extensive experimental results and experimental details presented in the manuscript reflect the comprehensive work of the authors. 

Clarity: The paper effectively communicates its ideas and findings with clarity. The paper is well-written, and the logic is coherent. The experimental settings and findings are structured and easy to find the related contents. 

Significance: The paper focuses on improving representation learning for proteins as a foundation model for multiple downstream tasks. The model proposed in the manuscript is able to encode sequential and structural data, and surpass baselines on many downstream tasks, illustrating its potential in even more applications in protein design and discovery.

### Weaknesses
1. Although the paper is well-written, logically coherent, and self-consistent, I'm afraid the novelty of the paper is not too high. The pertaining strategy which combines sequential and structural information is not new to the field. Furthermore, the major contribution of the paper, which is encoding both the atom-level and the finer-grained distance information, has also been studied extensively in recent years. Therefore, I cannot be persuaded of the novelty of the manuscript unless the authors can provide more evidence about how their model differentiates from existing methods and how their adaptations contribute to the enhanced model performance. Specifically, the paper lacks a clear articulation of how its approach to integrating sequential and structural information differs fundamentally from existing methods that also leverage both modalities. The use of distance information, while valuable, is not unique, and the paper needs to demonstrate a novel mechanism or representation that sets it apart. The claim of capturing both atom-level and finer-grained distance information needs more concrete examples of how this is achieved and why it is superior to other methods that also encode distance information. Without a more detailed explanation of the specific architectural innovations or unique training strategies, the novelty remains questionable.


### Questions
1. For pretraining experiments, I'm wondering how the noise level is determined. Besides, I'm wondering whether the authors have evaluated the data efficiency of the proposed pertaining approach by varying the pertaining data sizes. 

2. For fine-tuning experiments, are the encoder parameters also fine-tuned or frozen? Besides, since the focus of this paper is to evaluate the capability of the encoder and the decoders are already lightweight, why not simply fix the decoder architecture for every downstream task?

3. The authors mention in the conclusion that "... an efficient pre-training model ...", but I'm wondering how the "efficiency" is illustrated: does it enhance model performance, have less computation cost, or require less training data?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a general architecture for protein representation learning, utilizing a pre-training method of masked residue type prediction. Following this, the model is fine-tuned using lightweight decoders for a range of downstream tasks such as model quality assessment, binding affinity change prediction, EC and fold classification, protein design, and antibody design. It manages to achieve state-of-the-art performance in certain areas.

### Strengths
The paper's ambition to create a universal protein pre-training model is commendable. Pursuing this aim, the author presents a transformer architecture that seamlessly integrates sequence and structural data through a straightforward pre-training objective.

### Weaknesses
1. The majority of the components within the proposed method are adaptations from prior studies, which the paper fails to acknowledge. The transformer approach mirrors that of [1], and the pre-training objective resembles [2]. Consequently, the work's novelty is somewhat questionable.
2. The paper's "related work" section is not exhaustive. Notable omissions in the protein language domain include TAPE [3], ProtTrans [4], Ankh [5], and ProGen2 [6]. Additionally, recent advancements in protein structure representation, such as ProNet [7] and CDConv [8], are overlooked. A discussion on the connection between this study and previous ones is conspicuously absent.
3. The presented experimental results have serious issues like data leakage and the absence of critical baselines, undermining the paper's claims.

For details, please refer to the Question section.



### Questions
1. The authors motivate the use of transformers as encoders by critiquing graph-based representation learning methods for two reasons: 1) their inability to capture detailed atomic information, and (2) their disregard for long-range interactions. However, recent studies [7,9,10] demonstrate that graph-based methods can indeed be extended to the atom level. Additionally, the authors' method focuses solely on backbone-level structures, thus overlooking side-chain details. Regarding long-range interactions, the paper lacks experiments substantiating their claim. Thus, the critiques they raise against graph-based methods lack evidence.
2. It's inadvisable for the authors to describe their method as "groundbreaking" in the introduction—this is a clear exaggeration.
3. The model quality assessment, used by the authors for evaluation, has a potential data leakage risk during pre-training. This task aims to predict the GDT-TS score of certain model predictions without revealing the ground-truth structures. Yet, using the PDB data up to May 1st, 2023, means the model may have encountered target structures from CASP14 and CASP15 during pre-training. Despite different loss functions, this could pose a significant issue.
4. In the model quality assessment, the authors omit essential baselines. Notably, this task has been included in the Atom3D benchmark [11], where baselines [9,12] are essential references.
5. For binding affinity prediction, the authors neglect to explain their dataset splits—critical to avoid data leakage. Given the small test datasets, it's standard to conduct multiple cross-validations under varying random seeds. Traditional methods like FlexDDG [13] should also be considered for comparison.
6. In the EC and fold classification benchmarks, there's an absence of vital baselines, notably CDConv [8] and ESM-GearNet [14]. The authors might also explore the more challenging GO prediction tasks detailed in [15]. Even without these benchmarks, the authors' method falls behind leading approaches.
7. For protein design tasks, there are serious data leakage problems due to the presence of test data in pre-training dataset. As discussed in App. E.3, such leakage can dramatically affect performance. The authors have not provided a fair comparison with other methods, which makes the evaluation here not convincing.
8. In both protein and antibody design tasks, the metrics of perplexity and aar have been misleadingly employed in the field to evaluate protein folding models. The focus of these metrics on "local" recovery rather than entire sequences can inflate performance figures. A more accurate gauge would be to use the AF2 metric to assess structure recovery.

Overall, I commend the authors' ambition to introduce a universal model for protein-related tasks. However, their review of prior works appears incomplete, and the comparisons in their experiments lack rigor. Consequently, this paper does not meet the acceptance standards of ICLR.

[1] Shan et al. “Deep learning guided optimization of human antibody against sars-cov-2 variants with broad neutralization”, PNAS, 2022

[2] Zhang et al. “Protein representation learning by geometric structure pretraining”, ICLR, 2023

[3] Rao et al. "Evaluating protein transfer learning with TAPE." NeurIPS, 2019

[4] Elnaggar et al. “Prottrans: Toward understanding the language of life through self-supervised learning”, PNAS, 2021

[5] Elnaggar et al. “Ankh: Optimized Protein Language Model Unlocks General-Purpose Modelling”, 2023

[6] Madani et al. “Large language models generate functional protein sequences across diverse families”, Nature Biotech, 2023

[7] Wang et al. “Learning Hierarchical Protein Representations via Complete 3D Graph Networks”, ICLR, 2023

[8] Fan et al. “Continuous-Discrete Convolution for Geometry-Sequence Modeling in Proteins”, ICLR, 2023

[9] Jing et al. “Equivariant Graph Neural Networks for 3D Macromolecular Structure”, 2021

[10] Zhang et al. “Pre-Training Protein Encoder via Siamese Sequence-Structure Diffusion Trajectory Prediction”, 2023

[11] Townshend et al. “ATOM3D: Tasks On Molecules in Three Dimensions”, NeurIPS Dataset and Benchmark Track, 2022

[12] Pages et al. “Protein model quality assessment using 3d oriented convolutional neural networks”, Bioinformatics, 2019

[13] Barlow et al. "Flex ddG: Rosetta ensemble-based estimation of changes in protein–protein binding affinity upon mutation." The Journal of Physical Chemistry, 2018

[14] Zhang et al. “Enhancing protein language models with structure-based encoder and pre-training“, 2023

[15] Gligorijevic et al. “Structure-based protein function prediction using graph convolutional networks”, Nature Communications, 2021

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
