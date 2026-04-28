# Audio Prototypical Network for Controllable Music Recommendation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Traditional recommendation systems represent user preferences in dense representations obtained through black-box encoder models. While these models often provide strong recommendation performance, they lack interpretability for users, leaving users unable to understand or control the system’s modeling of their preferences. This limitation is especially challenging in music recommendation, where user preferences are highly personal and often evolve based on nuanced qualities like mood, genre, tempo, or instrumentation. 
    In this paper, we propose an audio prototypical network for controllable music recommendation. This network expresses user preferences in terms of prototypes representative of semantically meaningful features pertaining to musical qualities. We show that the model obtains competitive recommendation performance compared to popular baseline models while also providing interpretable and controllable user profiles.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to tackle the task of controllable music recommendation. It leverage music clip level prototypes as explanations and propose an attention-based recommendation model to fulfil the task. Experiments are conducted to demonstrate how this method performs the control during recommendation. Multiple experiments illustrate several properties of this method.

### Strengths
* The task of controllable music recommendation is valuable in both academia and industry. 
* The motivation of using music-clip level prototypes is reasonable and clear. And the way to directly use music content for recommendation is a promising direction.
* The writing is clear and easy to follow.

### Weaknesses
1. Less technical novelty: 
* The proposed prototype-based controllable music recommender model is a quite straightforward attention-based neural network model with certain losses. The attention-based model architecture has been proposed and extensively studied in recommender systems, which even though is practical and helpful,  it is not quite novel to the research or industry community. Specifically, the use of attention to weigh different prototypes is a common practice, and the novelty of this specific application is not clearly articulated. The paper would benefit from a more in-depth discussion of how this particular attention mechanism differs from existing approaches in recommendation systems.
* The learning or extraction of the prototype is based on some existing methods (MERT or MusicGen). I am expecting certain innovations in this part, which is quite interesting. For example, is it possible to automatically mine such prototypes purely based on user behaviours’ data as supervision? Furthermore, the music understanding model that is used to extract such prototypes should also be optimized during this process (in either end2end or multi-stage manners)? The paper lacks a discussion on the limitations of using pre-trained models for prototype extraction, and how this might affect the overall performance and controllability of the system. There is no exploration of alternative methods for prototype generation or adaptation.

2. Lacking rigorous evaluation:
* Only one dataset. I understand that it is not easy to obtain many datasets pertaining to this task formulation, while only using one dataset is less convincing to justify the generalization capability of the proposed method. The paper does not discuss the specific characteristics of the Million Song Dataset that might make it suitable or unsuitable for this task, nor does it acknowledge the potential biases inherent in this dataset. The lack of experiments on diverse datasets limits the conclusions that can be drawn about the robustness of the proposed method.
* The baselines are just general music recommendation models, which could be weak. Explainable recommendation is a quite popular topic in the past few years, and I assume there should be quite a number of works that can be implemented or adapted to this task, while they are not included in this paper. In addition to performance comparison with baselines, the controllability comparison with baselines should be also considered. The paper needs to include a more comprehensive comparison with state-of-the-art explainable recommendation methods, particularly those that focus on music or audio. The current baselines do not adequately address the specific challenges of controllable recommendation.
* For Section 5.5, there are many cold-start recommendation methods that can be implemented as baselines. I hope you can select some methods to do a comparison study instead of only comparing with the model itself in the non-cold start setting. The paper should have included a comparison with established cold-start recommendation techniques to demonstrate the effectiveness of the proposed method in this challenging scenario. The current evaluation does not provide a clear picture of how the method performs relative to existing cold-start solutions.
* Even though the target of this paper is the controllability rather than overall performance, it is still a concern that the quantitative performance of the model is not very strong.

### Questions
Please see the above comments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a music recommendation method based on audio prototypes. The method first inputs the music tags into the music generation model to generate the corresponding audio; then the MERT model is used to extract the final feature of 1024 dimensions of each generated audio. During the training process, each song in the user's behavior obtains the weighted representation of tag-audios through attention network; the user's representation is the sum of all behaviors(songs) and used for recommendation in final.

### Strengths
1. This paper attempts to use audio features for music recommendation to solve the problem of insufficient keywords/tags problem.
2. This paper proposes a metric to test the controllability of the model.

### Weaknesses
1. Although the author proposes that the model is controllable, the review is not clear about the definition of controllability in the paper, and the comparison between the model and other baseline methods (only one), and where its controllability is superior. Specifically, the paper lacks a clear, quantitative definition of controllability. The reviewer is unsure how the proposed metric (change in NDCG) directly measures the model's ability to be controlled by specific tags. Furthermore, the comparison with only one baseline, SEM-MacridVAE, is insufficient to demonstrate the superiority of the proposed method in terms of controllability. The paper should include comparisons with other relevant methods and provide a more detailed analysis of the controllability metric.
2. There are many classic CF methods and DL-based methods for recommendation based on user behavior. The reviewer noticed that the paper only selected VAE-based methods for comparison without any explanation or motivation of such selection. The paper should justify why VAE-based methods are the most appropriate baselines for comparison. The lack of comparison with other types of recommendation methods, such as collaborative filtering or other deep learning approaches, raises concerns about the generalizability of the results. The paper should include a more comprehensive set of baselines to demonstrate the effectiveness of the proposed method.
3. The paper emphasizes the use of prototype audio of music for recommendation. These audios are generated by the original tags of the music via MusicGen, but the author does not explain the details and settings of the generation process, not provide analysis and distribution of the generated audio, and cannot provide proof of whether there is an essential difference between these audios and the original tags in the role of recommendation, nor does it provide comparative experiments to prove the difference between the two. Therefore, the review cannot determine that the paper solves the limitation problem of tag-based recommendation proposed by audio-based recommendation. The paper needs to provide details on the MusicGen settings, analyze the distribution of generated audio features, and conduct experiments to compare the performance of tag-based and audio-based prototypes. Without these analyses, it is difficult to assess the contribution of using generated audio.

### Questions
The main questions are the problems listed in the weakness. In addition, there is a technical question in line140 equation 3 and line148 equation 4. Are the  $x^i_j$  in the two equations the same or not? How is the query $x^i_j$ in the attention represented?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a prototype-based network for explainable recommendations. The key model pipeline involves (1) prototypes generated by a controllable music generation model (MusicGen), (2) transformed user history into an interpretable sequence, where multi-head attention was used to learn the weight distributions over prototypes, and (3) a feed-forward neural network for the recommendation task as an extreme classification problem, where two auxiliary objectives accompany the recommendation objective: a controllability objective to impose calibration of user-level tag preference, and a prototype-separability objective to avoid prototype collapse. 

The experiments were conducted on MSD, a commonly used music recommendation dataset. The paper claims improvements in controllability through their proposed metric, which is calculated based on the difference of tag-wise ranking after removing certain prototypes, while maintaining competitive performance to the compared recommendation baselines.

### Strengths
This paper introduces an interesting perspective on combining prototype networks and the controllability of recommendations. The fact that the prototypes were interpretable (i.e. listenable music clips) is a nice feature, and the controllability is measured by the calibration of user tag preferences also provides a direct way to implement user controls. 

The experiments seem to indicate the effectiveness of the added two objectives by improving the recommendation performance. The authors further analyzed the tag-wise performance drop to support the importance of these prototypes. A series of ablation studies were conducted to study the importance of model parameters.

### Weaknesses
The method lacks novelty: each component of the whole model is not new. The key concept of using prototypes for explainable recommendations has been explored in [1]. Different from [1], the number of prototypes is fixed in this paper and aligned with pre-defined song tags, which can limit the expressiveness of the model and may suffer from noisiness in tag data. The quality of these prototypes is delegated to a generative music model, but the experiments do not address details on how the quality may affect model training and controllability.

The baselines compared is rather limited: To show the recommendation performance is competitive, the authors shall also compare models with reported superior performance on the MSD dataset such as [2] (as reported in the RecVAE paper) to provide more references. I also recommend the authors consider comparing to ProtoMF [1], since method-wise they also used the concept of prototype network for recommendations.

### Questions
1. Can you explain more about the process of prototype generation, in terms of why choosing a certain generative model, the diversity (similarity between generated prototypes), and quality (tag-music alignment) of the generated prototypes? Furthermore, how it may affect the performance of the resulting recommendation model? 

2. Can you further elaborate on the ablation study on training loss components (sec 5.4), in particular, was the monotonically increasing recommendation performance suggesting the recommendation model without the regularization terms was badly trained? If you add more searches on $\lambda_{1}$ and $\lambda_{2}$, will you see a tradeoff between the multiple objectives?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a "prototypical network" for music recommendation, which basically expresses user preferences in terms of a combination of listenable prototypes (i.e., short musical snippets). This is argued to be a more interpretable and controllable form of music recommendation as the tags (and snippets based on them) are interpretable and weighted preferences are controllable by the user.

### Strengths
The idea of using listenable prototypes to improve the interpretability of music recommendation is (to me) original, at least in the context of music recommendation.

### Weaknesses
Ultimately the prototypes did not strike me as convincing, and I didn't see additional value in them compared to more traditional tags. The generated audio did not seem to be faithful to the tags (e.g. music with male vocalist didn't have any vocalist -- this was just the first one I tried). So I'm not really convinced that "listenability" really adds to the usefulness of the method compared to a (presumably more trivial) approach purely based on tags. I'm not sure I generally see the value of a generative approach in this context, compared to e.g. extractively choosing snippets from songs a user likes. As a user it would be difficult for me to express my preferences in terms of these listenable snippets which often did not sound like "real" music.

Performance is also probably a sticking point. The authors acknowledge that the method is competitive with, but not stronger than baseline methods, and offer increased controllability to overcome this shortcoming. But I think that requires that the controllability / interpretability claims are totally convincing, which they aren't quite yet.

### Questions
-- Why does the approach need to be generative (abstractive) rather than extractive?

-- Is it possible to more directly compare against the strongest baselines on MSD? I understand there were some issues here since not all the songs contain audio and the dataset had to be sampled (and baselines rerun) but I am maybe missing a summary of whether the performance is really close to SotA for this dataset.

-- From the user perspective, what is the value of this system compared to just surfacing the tags themselves? To the extent that the tags *don't* match the snippets, the system isn't faithful and will confuse users. To the extent that the tags *do* match the snippets, the snippets are (arguably) redundant.

### Soundness
3

### Presentation
2

### Contribution
2
