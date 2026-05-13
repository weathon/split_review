# InterDance: Reactive 3D Dance Generation with Realistic Duet Interactions

- Decision: Reject
- Scores: 6, 6, 6, 5, 5

## Abstract
Humans can perform a variety of interactive motions, among which two-person dance is one of the most challenging interactions. However, in terms of computer motion generation, current work is still unable to generate high-quality interactive motion, especially in the field of duet dance. On the one hand, this is caused by the lack of large-scale high-quality datasets. On the other hand, it arises from the incomplete representation of interactive motion and the lack of fine-grained optimization of interactions. To address these challenges, we propose a duet dance dataset that significantly enhances motion quality, data scale, and the variety of dance genres. Based on this dataset, we propose a new motion representation that can accurately and comprehensively describe interactive motion. We further introduce a diffusion-based algorithm with an interaction refine guidance strategy to optimize the realism of interactions progressively. Experiments demonstrate the effectiveness of our dataset and algorithm. Our project page is https://inter-dance.github.io/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a mocap dataset for couple dances, a novel motion representation that takes contact into account, and a diffusion-based model for predicting conditional motion during couple dance.

### Strengths
* The proposed mocap dataset is a good contribution to the community especially as it contains enough fine-grained information to capture contact points between people.
* The proposed motion representation prioritizes correctly predicting contact, something that is often missing from similar works.
* The proposed diffusion-based method seems to achieve competitive results (though see weaknesses and questions for issues with the evaluation methodology).

### Weaknesses
 * Evaluation:
    * Simple strong baselines missing from the quantitative and qualitative experiments:
        * Return a NN motion clip of a follower from the training set where the distance is calculated based on motion-based distance
        * Return a NN motion clip of a follower from the training set where the distance is calculated based on a SOTA music embedding distance
        * Mirror the motion of the leader.
    * Metrics:
        * Missing a measure of correlation between the dancers in comparison to ground truth (see questions below)
    * Baselines:
        * Missing an apples-to-Apples comparison with existing baselines on the datasets on which they were trained:
            * Result tables in main and appendix only seem to test Duolando on the InterDance dataset or train the proposed method on DD100 (Table 3 in the appendix E) but I couldn’t find an apples-to-apples comparison of the proposed method trained and tested on the existing DD100 to Duolando trained and tested on DD100 (allowing Duolando to be tested on the dataset on which it was trained.
            * This apples-to-apples comparison is crucial in the case of Duolando which learns a motion codebook from training data and therefore is not suited to be tested on out-of-distribution dance genres. 
* Exposition:
    * Missing some implementation details for the experimental setup (see details below in the questions section)
    * Missing details of the user study: where were participants recruited from, how were they compensated, in what format were videos presented, in what resolution, was music included and did the experimenters verify it was in use, etc.
* Smaller notes:
    * The caption of Table 1 is not entirely factual as stated since InterHuman has Strong interaction and a longer total duration: “Among duet dance datasets with strong interaction, InterDance features the widest range of 15 dance genres, the longest average duration per sample at 142.7 seconds, and the longest total duration of 3.93 hours.”
* Limitations:
    * Limitations are not properly discussed. As in all studies, there are limitations in both dataset and method. These are to be expected, but should also be mentioned. 
        * The dataset is indeed larger than existing mocap ones, but is still a small dataset when compared to methods that can rely on image-based 3D lifting. There is a balance here between data quality and quantity, but that should be mentioned.
        * There are limitations to using diffusion-based generative models for motion prediction in comparison with autoregressive methods, namely the full trajectory is predicted at once, without training to predict longer sequences in a sliding-window fashion.
        * This is the only limitation mentioned: “The potential societal impact is that, as dance generation and human interaction technology become more advanced, highly realistic virtual humans might lead users to become so immersed in the virtual world that they detach from real-world participation.” (L 531). However, if this technology becomes more advanced, more imminent limitations may present themselves. Namely, music-to-dance and person-to-person prediction of dance may be used by AI systems to replace human dancers and choreographers, leading to a less creative human kind and numerous copyright issues.

### Questions
* Dataset: why not combine with DD100 to create a larger total dataset?
* Motion representation: if the root translation and angle is modeled jointly with the body pose (joints and vertices) it seems to me that translation, orientation, and pose would be coupled together. i.e. a person lifting their leg at point A in space would need a different representation then a person lifting their leg in the same way at point B in space. This seems to lead to needing more data in order to learn motion priors from the data as opposed to representations that would decouple pose from location and orientation. I am not listing this as a limitation yet as I would like to hear your thoughts about this issue. Would you be so kind as to explain this to me?
* Evaluation:
    * Metrics:
        * How is FID calculated?
        * While cross distance captures the distance between the two dancers, I am missing some measure of the correlation between the motion dynamics of the two dancers (see, for example paired FD here: https://arxiv.org/pdf/2204.08451). Do you think that cross distance captures this already somehow? If so, please explain. If not, I would suggest adding a measure of correlation in comparison to the ground truth correlation.
    * Baselines:
        * how are Edge and InterGen modified for benchmarking on this task (as they were designed a trained for different tasks)? Details are not given in the manuscript.
        * Was Duolando trained on the proposed InterDance dataset for the experiments presented? Or was it trained on its original DD100 dataset and tested on InterDance?
        * The following explanation regarding the performance of Duolando is cryptic to me. Please explain what you meant by it (line 421) “Compared with Duolando, which is carefully designed for reactive dance generation, our method performs better in most metrics. This is because Duolando employs a two-stage training framework that stores motions in a codebook, making it difficult to optimize fine-grained interactions.”
* Result videos:
    * Are the result videos on unseen test examples or from the train/val set?
    * Are the other methods in the result videos tested on the newly proposed dataset or on their original datasets on which they were trained? Was testing conducted on the test sets of the other methods in comparison?
    * Why is EDGE not in the results videos?
    * Please provide results also on randomly-chosen (rather than cherry-picked) examples.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new duet dance dataset that includes a variety of dance genres and features high-quality motion capture (MoCap) data. This dataset is larger in scale compared to previous ones. The authors also propose a new motion representation designed to better capture interactive movements, implemented within a novel diffusion-based framework. Experimental results demonstrate the effectiveness of both the new dataset and the proposed algorithm.

### Strengths
The overall paper is well written and structured. 
1. The new dataset captures detailed body and finger movements, which are valuable for the motion generation community.
2. The proposed motion representation includes multiple components: positional space, joint data, hand movements, surface information, and canonical space. This combination aims to make generated motions more realistic.
3. The authors propose a diffusion-based model for reactive dance motion generation, incorporating an Interactive Refine Guidance mechanism to improve the accuracy and realism of interactive dance movements.

### Weaknesses
However, there are several areas for improvement:

1. Since the dataset is a major contribution of this paper. The dataset description should include not only the total hours of data but also detailed information on the number of frames and sequences for each category. 

2. For the 655 vertices used in the study, how were they selected from SMPL-X? Were they sampled randomly or in a way that preserves the topology?

3. $L_f$ for foot contact loss is not clearly stated.

4. The symbol $f$ is used in two different contexts in the paper: it denotes foot contact in Equation (1) and forward motion in Equations (2), (3), and (4).

5. One important realted work [1] is missing.
[1] Listen, denoise, action! Audio-driven motion synthesis with diffusion models. SIGGRAPH 2023.

6. Line 72     priors, without -> prior without

### Questions
For the dataset, 1) Compared to text-to-motion datasets, does each category in this dataset feature multiple pairs of dancers, or just one pair per category? 2) Since human participants were involved in data collection and the data will be released in the future, did all dancers sign consent forms?

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
The paper study 3D dance generation. It introduces a large-scale duet dance dataset. To better model interactive motion, it also presents a motion representation method and an enhanced diffusion-based framework featuring an interaction-refined guidance sampling strategy.

### Strengths
### Originality
The originality of the paper are from three aspects:
1. a new large-scale dataset;
2. a new motion representation;
3. an interaction refine guidance sampling strategy.

### Quality
The generation results are good, especially visual outcomes. And the experiments are comprehensive, which can well validate the paper's claim. Furthermore, the code and project page will be released to enhance the reproducibility.

### Clarity
The paper is well-organized, and all the concepts are explained clearly. Furthermore, the technical details are also presented clearly.

### Significance
The proposed dataset is good for duet dance generation, and the introduced motion representation and sampling strategy are essential for more effectively modeling interactive motions.

### Weaknesses
The reviewer does have some concerns as listed below:

1. There is a lack of comparison with state-of-the-art (SOTA) methods on the DD100 dataset.

2. According to the ablation study, it appears that $L_{RO}$ and Vertices may hinder motion quality.

3. I disagree with the paper's assertion that "more interaction brings more penetration." I believe a well-designed model should enhance interaction without a corresponding increase in the penetration rate. Therefore, it would be better that the paper develops a new metric that integrates both penetration rate (PR) and contact frequency (CF) to better assess the model's performance.

4. The novelty of the method warrants concern. Regarding the dataset, while the proposed dataset is twice the size of the existing DD100 dataset [1], I don't believe it offers substantial improvements for this task. As for the method, the proposed motion representation seems to be a trivial combination of two existing representations [2, 3]. For the sampling guidance strategy, I recommend that the paper cite related works, as using gradients to guide the denoising process is a common practice in diffusion-based generation. In conclusion, it would be better that the paper pays more attention to clearly articulating the novelty and uniqueness of the proposed dataset and methods.

These weaknesses may diminish the overall contribution of this paper.

### Questions
Please respond to the concerns above.

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
4

### Summary
The submission aims to tackle the generation of duet dance motions, where the modeling of two-person interactions is challenging. To this end, the authors introduce a duet dance dataset featuring body and finger movements with high physical realism, comprising 3.93 hours of music-paired duet dance across 15 different dance genres. In addition, the authors also propose a diffusion-based reactive dance motion generation model with a dedicated module - Interactive Refine Guidance - to enhance the accuracy and realism of interactive dance movements.

### Strengths
As always, I admire the contribution made by the authors on the data collection. The duet dance dataset could contribute to the motion generation field, facilitating more future works.

Overall, the paper is well-structured, well-written, and easy to follow.

The submission contains a sufficient number of quantitative evaluations.

### Weaknesses
The generated results are not convincing, especially in terms of the interaction between the two performers. See the first on the left of Figure 7, the final generated result (after) has a wrongly placed arm of the blue character, which should presumably hook around the back of the waist of the other performer. And several other results also show incorrect hand interactions. And from the supplementary video results I got an impression that the results of the proposed method do not have significant improvements over those of Duolando. A similar conclusion could also be derived from Table 3, Duolando has similar numbers with Ours, some even better.

The submission lack core technical contributions. While the motion representation described in Section 4.1 makes sense to me, it is not novel. Actually I was wondering whether it is true that the leader's motion representation contains the contact label or not. If yes, requiring contact information from the leader performer could be problematic when applying the trained model in a real-world scenario. Moreover, the Interaction Refine Guidance is not of significant technical contribution either.

Lack of sufficient qualitative results. I would be better to provide more qualitative results, including more comparison results, ablation study results, etc. The numerical numbers sometimes could be inconsistent with the visual results.

### Questions
In Section 5, the description of metrics calculation is not rigorous. Is the FID computed by measure the distance between one generated motion and its associated GT motion? Following that, how come the FID computed from the GT set is not 0 - correct me if I am missing anything.

Is it true that the motion representation of the leader includes the contact label?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce a new large-scale duet dance dataset, which contains 3.93 hours of duet dance mocap data across 15 different music genres. Based on this new dataset, this paper developed an algorithm for dance reaction generation. Specifically, a novel representation on the top of both body vertices and skeleton features is used, and the vanilla diffusion model with classifier guidance is applied for dance motion synthesis. User study, ablation study, and quantitative evaluations are conducted to demonstrate the effectiveness of the proposed framework.

### Strengths
**1. The dance dataset is valuable to the community**. This paper proposes a large-scale and high-quality two person dance dataset. Capturing dance motions are expensive and laborious. This will definitely be a nice asset for the community. I appreciate the nice visualization and analysis of the dataset. From table 1, it's well to know this dataset is almost twice the size of the existing largest duet dance dataset, DD100.  
**2. Incorporate both body shape and skeleton is a nice touch**. Compared to previous method, this paper propose a new motion representation with both body shape information and skeleton features. Intuitively, this might help on close interactions.   
**3. Inference time guidance on penetration and contact is interesting**. The inference time classifier guidance, if being used properly, seems like a nice trial to avoid penetration and contact as a plugin method.       
**4. Content is well-organized**. Presentation is clear and easy to follow.   
**5. Comprehensive quantitative evaluations.**

### Weaknesses
 **1. Limited significance and contribution**. This work is not the first one in either duet dance reaction synthesis or duet dance dataset. Though this dataset is larger than the existing one, the overall setting are basically the same and the method are principally a vanilla diffusion model, whose novelty is incremental. The core contributions, a larger dataset and a reactive generation method, have both been explored in prior work. While the dataset is larger, a 2x increase in size doesn't necessarily represent a significant leap, especially if the data characteristics and diversity are similar. The method, while incorporating body shape, still relies on a standard diffusion framework, lacking substantial methodological innovation. The claim of improved contact handling is not convincingly demonstrated through visual results, and the generated interactions still appear somewhat artificial.

 **2. Importance of the task is questionable**. It's not clear why it is important to research on reaction generation, especially for duet dance. In my opinion, the individual dance movements in a duet dance are highly correlated, where each motion alone make little sense. I can not figure out any application that needs to generate the reactive dance movements. It will be more practical to generate movements for both individuals. Though the current method supports generations for the dance of both two individuals, the results looks rather unnatural. The reactive generation task, which is the main focus, seems less practical given the strong temporal and semantic dependencies between dancers in a duet. Generating one dancer's motion based on the other's feels like an artificial constraint, as the movements are inherently co-created. The simultaneous generation, while mentioned, is not the core focus and the results are not compelling enough to justify the reactive approach.

 **3. Short dance generation**.  From the results, it seemed the model can not generate quite short dance clips, e.g., 4s. Could the model be scaled to longer sequence? The presented results appear limited to short clips, raising concerns about the model's ability to handle longer, more complex dance sequences. The lack of analysis on performance across different sequence lengths makes it difficult to assess the model's practical applicability.

 **4. Insufficient qualitative results**. There are only very few examples for generated results. There are no results for ablation analysis either. It's hard to confirm if the proposed components works as claimed. The limited number of qualitative examples makes it difficult to assess the quality and diversity of the generated motions. The absence of visual ablation studies further hinders the evaluation of the proposed components, making it hard to verify the effectiveness of the claimed improvements.

### Questions
Please refer to the weakness sections.

**Significance**:  the authors need to justify the importance and potential applications of reactive dance generation. Specifically, elaborate on potential use cases or scenarios where generating reactive dance movements could be valuable.

**Short length**:  could provide results or analysis on the model's performance across different sequence lengths, from very short (e.g. 4s) to much longer durations. This would give a clearer picture of the model's scalability.

**Insufficient results**: More diverse examples of generated results across different dance styles and interaction types
Visual comparisons for the ablation studies to illustrate the impact of different components
Failure cases or limitations of the current approach.

### Soundness
2

### Presentation
3

### Contribution
2
