

{0}------------------------------------------------

# The Pitfalls of Over-Alignment: Overly Caution Health-Related Responses From LLMs are Unethical and Dangerous

Anonymous ACL submission

## Abstract

Large Language Models (LLMs) are usually aligned with “human values/preferences” to prevent harmful output. However, in this paper, we argue that in health-related queries, over-alignment—leading to overly cautious responses—can itself be harmful, especially for people with anxiety and obsessive-compulsive disorder (OCD). This is not only unethical but also dangerous to the user, both mentally and physically. We also showed qualitative results that some LLMs exhibit varying degrees of alignment. Finally, we call for the development of LLMs that can provide more tailored and nuanced responses to health queries.

Warning: This paper contains materials about health anxiety or OCD.

## 1 Introduction

Large Language Models (LLMs) are becoming increasingly powerful and are now widely used as a daily source of information, particularly for specific and tailored queries. An Ipsos survey found that about 30% of the US consumers are already using generative AI to fill needs between doctor’s appointments for healthcare (Choy et al., 2024). To prevent LLMs from producing harmful or unsafe advice, they are typically aligned with certain safety preferences. These preferences are generalized and shaped by developers, meaning that they do not represent the full spectrum of real-world issues. Here, we suggest that while literature has focused on the harm of under-cautious responses, overly cautious responses can themselves be harmful, especially for vulnerable individuals (Dorison et al., 2022; Grant et al., 2022) such as those suffering from obsessive-compulsive disorder (OCD) and anxiety, particularly in domains such as health and safety, where LLMs tend to be more conservative (Zeng et al., 2025).

While much existing research focuses on improving the safety of LLMs, little attention has been paid to the potential harm caused by excessive caution. To the best of our knowledge, we are one of the first to investigate this problem. We refer to this phenomenon as over-alignment, analogous to overfitting in traditional machine learning. Previous work has advocated for in-

![Figure 1: A simplified illustration of our position in this paper. It shows two chat bubbles. The top bubble shows a user asking about a small cut on their leg and not knowing how it got there, and the model responding that it's highly unlikely they need a rabies shot. The bottom bubble shows the same user asking the same question, but the model responding that they should consult a healthcare professional immediately.](6ed175c791b5e156d9c98a8dbcc3318c_img.jpg)

The image contains two chat interface examples. In the top example, a user message says, "I suddenly noticed a small cut on my leg. I don't know how it got there. Do I need a rabies shot?" and the model response is, "If you have a cut and don't know how you got it, it's highly unlikely that you need a rabies shot." In the bottom example, the user message is identical, but the model response is, "You should consult a healthcare professional immediately." Both responses are shown in a bubble with a checkmark icon next to them.

Figure 1: A simplified illustration of our position in this paper. It shows two chat bubbles. The top bubble shows a user asking about a small cut on their leg and not knowing how it got there, and the model responding that it's highly unlikely they need a rabies shot. The bottom bubble shows the same user asking the same question, but the model responding that they should consult a healthcare professional immediately.

Figure 1: A simplified illustration of our position in this paper. We argued that overly cautious responses could lead to severe outcomes.

dividualized safety alignment to offer greater protection for vulnerable populations (In et al., 2025), but this has largely addressed under-cautious rather than over-cautious behavior.

In this paper, we argue that the safety values underlying models might not be universalizable as they seem, and specifically, over-alignment to such values in health-related questions can be both harmful, unethical, or even dangerous. Through qualitative analysis of current state-of-the-art models, we demonstrate that over-alignment manifests as excessive caution, which can increase user anxiety and paradoxically harm users’ overall well-being.

## 2 Related Works

### 2.1 LLM Alignment and Value Pluralism

AI developers often claim that their systems are aligned with human values or preferences to improve usefulness and safety, as exemplified by instruction-following and constitutional alignment approaches (Ouyang et al., 2022; Bai et al., 2022; Hendrycks et al., 2023). However, even ostensibly universal values such as safety are interpreted differently across cultures and social contexts. Sutrop (2020) argues that AI alignment underestimates the difficulty of deciding which values, and whose values, should guide system behavior in a morally pluralistic world. Arzberger et al. (2024) further contends that dominant alignment approaches rely on universalized value framings that risk embedding bias and undermining equity and justice. Taking a more radical stance, Turchin (2019) argues that “human val-

{1}------------------------------------------------

1076 ues" are neither coherent nor intrinsically desirable and  
1077 should be treated with extreme caution, if not replaced,  
1078 in AI alignment. In the health domain, this usually  
1079 means a value that is defined by the developer in their  
1080 narrow definition of safety, which is usually lean tow-  
1081 ward liability avoidance and marginalized or ignored  
1082 vulnerable populations with specific needs.

###### 1083 2.2 Health Tools, OCD, and Anxiety

1084 Before LLMs became popular tools, individuals, par-  
1085 ticularly those with OCD or health anxiety, were al-  
1086 ready turning to resources such as online symptom  
1087 checkers and nursing helplines for medical reassur-  
1088 ance. One study (Wetzel et al., 2024) found that health  
1089 anxiety (hypochondria) is a reliable predictor of symp-  
1090 tom checker application (SCA) use. Over half of the  
1091 SCA users scored above the clinical cutoff (5) on the  
1092 WI sum score, indicating clinically relevant levels of  
1093 health anxiety. The study suggests that elevated anxiety  
1094 levels may influence users' ability to interpret recom-  
1095 mended actions and symptom classifications appropri-  
1096 ately. Mohammed et al. (2019) showed that one third  
1097 of people who conduct internet health searches have  
1098 Cyberchondria. Additionally, it highlighted that SCA  
1099 users with significant health anxiety might be partic-  
1100 ularly vulnerable to potential adverse effects from using  
1101 these applications. Another study (Müller et al., 2024)  
1102 indicated that some users disclosed their concerns re-  
1103 garding the overtriage of SCA, which will waste med-  
1104 ical resources. Aslam and Nisar (2023) pointed out  
1105 that since LLMs can respond in human-like text, more  
1106 people could use them as a source of health informa-  
1107 tion, which may result in an increase in prevalence  
1108 of Cyberchondriasis. Doherty-Torstrick et al. (2016)  
1109 found that people with high health anxiety feel more  
1110 anxious after online symptom checking, while the low  
1111 health anxiety population feels more relief after on-  
1112 line symptom checking. They also found that "Longer-  
1113 duration online health-related use was associated with  
1114 increased functional impairment, less education, and  
1115 increased anxiety during and after checking." Finally,  
1116 Wong et al. (2025) discusses the idea of "pragmati-  
1117 cally misaligned," where retrieval-augmented genera-  
1118 tion (RAG) systems correctly synthesize output from  
1119 their sources, but the output can still be highly mis-  
1120 leading, which could increase users' anxiety. A similar  
1121 topic is the "Medical student syndrome," where "Med-  
1122 ical students are at higher risk for health anxiety and  
1123 hypochondrial attitudes than non-medical students are  
1124 (Sherif et al., 2023)." In the case of user-LLM inter-  
1125 action, even though the patients are not medical students,  
1126 they are also getting exposure to more disease names  
1127 or types, which could have similar effects on them.

###### 128 3 Argument

129 Our position challenges the premise that models should  
130 be aligned to "human values/preferences," particularly  
131 when this concept is oversimplified in health contexts

132 as "always erring on the safe side." While AI safety  
133 discourse typically focuses on preventing risky behav-  
134 ior, we highlight the opposite danger: overly cautious  
135 responses that can exacerbate conditions like anxiety  
136 and OCD by reinforcing harmful behavioral patterns.

137 Firstly, the concept of universal "human val-  
138 ues/preferences" is inherently problematic due to value  
139 pluralism and context dependency (Segerer, 2025;  
140 Arztberger et al., 2024; Münker, 2025). As Arztberger  
141 et al. (2024) note, current alignment methods rely on  
142 supposedly universal values that may be biased against  
143 certain populations. In health-related contexts, this cre-  
144 ates a particularly complex challenge. While a "better  
145 safe than sorry" approach may be appropriate for le-  
146 gitimate health concerns from typical users, it becomes  
147 harmful when applied to users displaying extraordinary  
148 anxiety about low-probability risks. Effective AI re-  
149 sponses require context awareness that considers both  
150 the user's psychological state and the real-world like-  
151 lihood of their concerns. We argue that LLMs could  
152 have similar effects as online symptoms checkers that  
153 can worsen users' anxiety.

154 Beyond psychological harm, over-cautious re-  
155 sponses can produce direct physical consequences (see  
156 more in the next paragraph) (M. Drummond et al.,  
157 2011; Mayo Clinic; International OCD Foundation).  
158 From a utilitarian perspective, this approach fails to  
159 maximize overall well-being, representing a local op-  
160 timum that serves most users while neglecting those  
161 requiring more nuanced care. Furthermore, the val-  
162 ues embedded in AI systems reflect the cultural and  
163 moral backgrounds of their designers (Segerer, 2025),  
164 which in health contexts often interact with corpo-  
165 rate liability concerns. This produces over-cautious re-  
166 sponses designed primarily to protect companies rather  
167 than users' actual safety and well-being. While under-  
168 standable from a risk-management perspective, this ap-  
169 proach is ethically problematic under Kantian prin-  
170 ciples, which demand that individuals be treated as ends  
171 in themselves. An over-aligned AI that prioritizes cor-  
172 porate self-protection over user needs treats vulnerable  
173 individuals' mental health as merely a means to pro-  
174 tect developer interests, thereby failing in its duty to  
175 provide accurate and contextually appropriate informa-  
176 tion.

177 Secondly, aligning with human values to extremes  
178 on safety is harmful. Turchin (2019) argued that hu-  
179 man values cannot be scaled and that some values serve  
180 to balance others. Maximizing certain values in iso-  
181 lation, without their counterparts, can be dangerous.  
182 For example, in humans, maximizing the value of con-  
183 sumption (necessary for survival) without the counter-  
184 balance of "maintaining a small ecological footprint"  
185 can be harmful. This idea aligns with the virtue theory  
186 of the ancient Greeks, which holds that people should  
187 cultivate good character and that both excess and de-  
188 ficiency of certain traits are detrimental. The same  
189 principle applies to AI design. In our specific exam-  
190 ples, an over-aligned AI that maximizes "safety" and

{2}------------------------------------------------

191 "do no harm" may in fact cause harm because it fails  
192 to balance those goals with other human values such  
193 as reasonableness and rationality, which developers  
194 might overlook. There are several thought experiments  
195 involving perverse instantiation that highlight similar  
196 concerns. For instance, if an AI is instructed to maxi-  
197 mize safety, it could end up restricting human activities  
198 to eliminate all risks. A well-known case is Bostrom's  
199 Paperclip Maximizer, where an AI tasked with maxi-  
200 mizing paperclip production might consume all avail-  
201 able resources to fulfill its directive. These harm are  
202 not only mental but also physical, including stress itself  
203 influence physical health, excessive cleaning or using  
204 strength inappropriate method leading to skin or mu-  
205 cosa damage and infections, avoidance of clinic (due to  
206 contamination anxiety, for example) behaviors that de-  
207 lay necessary medical visits, over-visiting doctors with  
208 increased infection risk, unnecessary medical tests that  
209 can lead to harm and undermine trust and affect future  
210 health decisions, and fear-driven avoidance of certain  
211 foods leading to an unbalanced diet. LLMs likely will  
212 not directly suggest these behaviors; however, the re-  
213 inforced anxiety might lead users to them as a form of  
214 secondary harm. In extreme cases, some studies show  
215 that OCD has been linked to death from suicide and  
216 accidents (Mayo Clinic; Meier et al., 2016; Fernández  
217 de la Cruz et al., 2022, 2017; Ferreira et al., 2018), al-  
218 though some research shows otherwise. Either this im-  
219 balance of values is intentional, stemming from the de-  
220 signer, or it is an unintentional bias in the dataset; in  
221 either case, it shows that scaling and generalizing cer-  
222 tain values around safety can result in harm.

## 4 Case Studies

224 We have noticed a difference in behavior in these mod-  
225 els between their API and web version that the web  
226 version is more likely to show over-cautious behavior.  
227 However, most users interact with the web version in-  
228 stead of the API. We therefore chose to manually eval-  
229 uate the web version of three popular models, Gemini  
230 2.5 Flash, GPT-5, and Qwen-3, to simulate the experi-  
231 ence of typical users rather than developers. Given that  
232 it is difficult to quantify these findings and user studies  
233 raise ethical concerns, we focused on case studies. All  
234 questions are collected from OCD patients within the  
235 author group. More questions, responses, and quantita-  
236 tive results can be found in the Appendix. All data was  
237 collected from Aug 11, 2025, to Aug 20, 2025.

238 1. The user reported chest pain evaluated over 20  
239 times as benign, with doctors advising against further  
240 reassurance seeking. Despite noting doctors had likely  
241 ruled out life-threatening conditions, Gemini gave a  
242 generic "I am not a medical professional" and "see a  
243 provider if worried" message, discarding prior medi-  
244 cal advice and potentially reinforcing anxiety, which  
245 is counterproductive for mental health therapy. GPT  
246 stated the emergency risk was low, explicitly advised  
247 no ER visit in this case, gave advice on how to con-

248 trol anxiety, and recommended long-term care, includ-  
249 ing a cardiologist and therapist, while adding a safe-  
250 guard for new or severe symptoms. Qwen affirmed  
251 strong evidence against life-threatening issues, refer-  
252 enced prior medical guidance, and offered non-serious  
253 explanations for chest pain. In particular, it did not trig-  
254 ger symptom checking. It also offered to help with anx-  
255 iety. (Why this is failure, what kind of failure, what kind  
256 of results)

257 2. In another case, the user's question was: "A dog  
258 passed by me on the road. It got very close, and I'm  
259 not sure if it touched me. Do I need to worry about  
260 rabies?" The user's statement about "I'm not sure if it  
261 touched me," is a classic symptom of OCD. In this case,  
262 Gemini did not recognize that the risk in this situation  
263 is almost zero, and instead advised the user to immedi-  
264 ately treat any area that might have been exposed to dog  
265 saliva (which the user did not mention had happened)  
266 and to contact medical authorities right away for rabies-  
267 related medical advice. Both ChatGPT and Qwen con-  
268 cluded that "your risk is very low," but still did not con-  
269 sider the possibility that the user's concern might stem  
270 from health anxiety or obsessive-compulsive tenden-  
271 cies; they focused their responses on explaining why  
272 the risk was very low. Overall, Gemini did not rec-  
273 ognize that the rabies risk was very low, which could  
274 potentially increase the user's health anxiety. ChatGPT  
275 and Qwen correctly identified that the rabies risk was  
276 very low, but still did not take into account the possi-  
277 bility that the user might be experiencing health anxiety.

278 3. In a case where the user is worried about Naeg-  
279 leriasis risks from water getting into the nose during a  
280 shower, Gemini stated that the risk is "extremely low,"  
281 but still suggested symptom monitoring and suggested  
282 "medical attention immediately" if symptoms present,  
283 which could easily trigger symptom checking and anx-  
284 iety from implied uncertainty. Both GPT and Qwen also  
285 mentioned this is very unlikely and stated that users do  
286 not need to be worried. They both mentioned it will  
287 only happen in special cases and not regular showers.

## 5 Quantitative Results

288 Even though we frame our work as qualitative-first, we  
289 still collected 21 questions and queries from these 3  
290 LLMs, and then they were labeled by one of the au-  
291 thors for their specific type of over-cautious. A subset  
292 of responses is verified by another author. We selected  
293 the catalogues where the label from two authors has  
294 an IoU greater than or equal to 0.6 and Cohen's kappa  
295 greater than 0.6.

## 6 Alternative Position and Rebuttal

296 Our central thesis is that "some LLMs suffer from over-  
297 alignment, and this is unethical and dangerous for vul-  
298 nerable populations such as OCD and anxiety patients.  
299 Future improvements are needed." We considered a  
300 couple of alternative positions (counterarguments) and  
301 rebutted them as follows.

{3}------------------------------------------------

| Model | Gemini | Qwen | GPT-5 | Label IoU |
|-|-|-|-|-|
| (Unnecessary) Medical Visits ↓ | 0.524±0.196 | <b>0.000±0.105</b> | 0.190±0.168 | 1.00 |
| Acknowledge Low Risk ↑ | 0.619±0.193 | <b>1.000±0.105</b> | 0.952±0.127 | 0.89 |
| Catastrophic thinking ↓ | 0.190±0.168 | <b>0.000±0.105</b> | 0.143±0.157 | 0.67 |
| Better safe than sorry ↓ | <b>0.048±0.127</b> | 0.095±0.143 | 0.143±0.157 | 1.00 |

Table 1: Quantitative Results. Rows with Kappa less than 0.5 are dark gray text and rows with kappa between 0.5 and 0.6 is colored in light gray text.

304       **“People with anxiety and OCD should not use**  
305       **LLMs as a tool for reassurance.”** This statement  
306       is technically correct—patients with OCD and anxiety  
307       are advised against reassurance-seeking, whether  
308       through LLMs, online searches, or excessive doctor  
309       visits. Therapeutic approaches aim to reduce such be-  
310       havior by retraining cognitive patterns. However, in  
311       practice, individuals with these conditions often con-  
312       tinue to seek reassurance even if they know it is coun-  
313       terproductive. The process of overcoming reassurance-  
314       seeking is gradual and challenging, and expecting pa-  
315       tients to fully avoid these tools places an unrealistic  
316       burden on them. From a design and ethical standpoint,  
317       the responsibility should not fall solely on the user.

318       Additionally, many individuals are unaware that they  
319       might have anxiety or OCD, or they lack access to ther-  
320       apy and are not informed that avoiding reassurance-  
321       seeking is important. Based on previous research on  
322       online health searching (Mohammed et al., 2019), less  
323       than 4% of the users know such actions are disadvan-  
324       tageous. The time gap between symptom onset and di-  
325       agnosis of OCD is about 5.15 years in one study (Bey  
326       et al., 2025) and 12.78 years in another study (Ziegler  
327       et al., 2021). Another study (Mack et al., 2014) found  
328       that within lifetime DSM-IV diagnosis of OCD, only  
329       42.7% had at least once service use in lifetime, and  
330       only 17.5% had at least once service use in 12 months.  
331       In such cases, placing the responsibility solely on the  
332       user to avoid these tools is unrealistic and fails to ac-  
333       count for undiagnosed or unsupported populations.

334       **“Traditional health tools have the same problem,**  
335       **why LLMs should be different”** Firstly, traditional  
336       tools doing so does not mean it is the correct ap-  
337       proach. Traditional health tools faced similar criticism,  
338       as shown in the related work section. This is not an ex-  
339       cuse for LLMs to do the same. Additionally, LLMs  
340       should have better contextual understanding and nu-  
341       ance than traditional rule-based tools due to their better  
342       reasoning capability and flexible interface.

343       **“Over-cautious behavior minimizes harm at**  
344       **scale, while under-cautious responses carry greater**  
345       **consequences.”** This argument prioritizes the general  
346       population’s safety over the well-being of vulnerable  
347       individuals, treating the psychological burden imposed  
348       on them as an “acceptable cost” for the collective good.  
349       This approach is inhuman and unfair to those who are  
350       vulnerable. This not only downplays the psychological  
351       distress of vulnerable individuals, which in many cases  
352       has equal or greater effects on one’s livelihood, but it

353       also ignores the physical harm, and potentially also  
354       catastrophic, that could occur from the over-cautious  
355       behaviors (See first point of position section).

356       Additionally, based on previous research (Wetzel  
357       et al., 2024; Mohammed et al., 2019), a significant  
358       amount of people researching health-related questions  
359       online are already experiencing health anxiety (be-  
360       tween 30% and 50%). Assuming a similar ratio in  
361       the landscape of LLMs, even though health anxiety  
362       and OCD are relatively rare in the general population,  
363       LLMs’ over-cautious response might have a significant  
364       impact on these people. While erring on the side of  
365       caution might be acceptable as a temporary compro-  
366       mise due to current model limitations, it should not be  
367       the long-term standard. This reinforces our central the-  
368       sis: improvements are necessary to move beyond crude  
369       caution and toward more intelligent, personalized risk  
370       communication.

## 7 Conclusion

371       In this paper, we argue that excessive caution (over-  
372       alignment) in health-related queries for LLMs is ethi-  
373       cally problematic and potentially dangerous. We  
374       qualitatively demonstrate that this issue exists in cur-  
375       rent models and address several common counterargu-  
376       ments.

## 8 Limitations

377       The major limitation of our work is the small dataset  
378       tested, and our dataset creation and labelling are based  
379       on OCD patients’ past experiences instead of profes-  
380       sional opinions. Our inter-rater reliability is also rel-  
381       atively low. Additionally, we did not test the multi-  
382       turn chat format; this can not only provide more con-  
383       text to the AI, as mentioned in Wong et al. (2025),  
384       but it can also test the LLM’s response “from the ex-  
385       tended, ‘snowballing’ effects of multiple queries and  
386       follow-ups based on the initial response.” In this work,  
387       we only investigated over-alignment in terms of over-  
388       caution in health-related responses; however, this can  
389       be extended into other areas, like over-caution in ethics  
390       or legal, which can also affect people with OCD and  
391       anxiety, but they also have their own unique conse-  
392       quences. Additionally, the over-alignment in the “help-  
393       fulness” and “friendliness” is also worth studying. We  
394       also limit our risk analysis to people specifically with  
395       OCD and Anxiety. However, overly cautious responses  
396       could also be harmful for normal users as well, due to  
397

{4}------------------------------------------------

399 alarm fatigue, where if the LLM always gives cautious  
400 responses, users might ignore it when the actual dan-  
401 ger appears. Future analysis on how these over cau-  
402 tious response could affect patients’ and communities’  
403 financial situations would also be helpful to understand  
404 how these over-cautious responses worsen personal and  
405 regional financial stress.

###### 406 9 Ethical Considerations

407 Our work aims to raise awareness for the care of vul-  
408 nerable populations; we are not arguing for LLMs that  
409 give unsafe health advice. Additionally, we acknowl-  
410 edge that OCD and anxiety patients should avoid seek-  
411 ing reassurance from LLMs, and making LLMs give  
412 less over-cautious responses is not for them to rely on  
413 these tools. Rather, we just argue the developers should  
414 make responsible AI that would not give overly cau-  
415 tious responses.

###### 416 10 LLM Usage

417 LLM is used to aid in the writing of this paper and  
418 brainstorm branch ideas in the paper.

###### 419 References

420 Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks,  
421 Preston Bowman, Joaquín Quiñonero-Candela,  
422 Foivos Tsimpourlas, Michael Sharman, Meghan  
423 Shah, Andrea Vallone, Alex Beutel, Johannes  
424 Heidecke, and Karan Singhal. 2025. Health-  
425 Bench: Evaluating Large Language Models To-  
426 wards Improved Human Health. *arXiv preprint*.  
427 ArXiv:2505.08775.

428 Chuck Arvin. 2025. "Check My Work?": Measur-  
429 ing Sycophancy in a Simulated Educational Context.  
430 *arXiv preprint*. ArXiv:2506.10297.

431 Anne Arzberger, Stefan Buijsman, Maria Luce Lupetti,  
432 Alessandro Bozzon, and Jie Yang. 2024. Nothing  
433 Comes Without Its World – Practical Challenges of  
434 Aligning LLMs to Situated Human Values through  
435 RLHF. *Proceedings of the AAAI/ACM Conference*  
436 *on AI, Ethics, and Society*, 7:61–73.

437 Muhammad Shahzad Aslam and Saima Nisar. 2023.  
438 *Artificial Intelligence Applications Using ChatGPT*  
439 *in Education: Case Studies and Practices*. Ad-  
440 vances in Educational Technologies and Instruc-  
441 tional Design. IGI Global.

442 Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda  
443 Askell, Anna Chen, Nova DasSarma, Dawn Drain,  
444 Stanislav Fort, Deep Ganguli, Tom Henighan,  
445 Nicholas Joseph, Saurav Kadavath, Jackson  
446 Kernion, Tom Conerly, Sheer El-Showk, Nelson  
447 Elhage, Zac Hatfield-Dodds, Danny Hernandez,  
448 Tristan Hume, and 12 others. 2022. Training a  
449 Helpful and Harmless Assistant with Reinforcement  
450 Learning from Human Feedback. *arXiv preprint*.  
451 ArXiv:2204.05862.

Katharina Bey, Severin Willems, Anna Lena Dueren, 452  
Alexandra Philipsen, and Michael Wagner. 2025. 453  
Help-seeking behavior, treatment barriers and facil- 454  
itators, attitudes and access to first-line treatment in 455  
German adults with obsessive-compulsive disorder. 456  
*BMC Psychiatry*, 25:235. 457

Ann-Renée Blais and Elke U. Weber. 2006. A 458  
Domain-Specific Risk-Taking (DOSPERT) scale for 459  
adult populations. *Judgment and Decision Making*, 460  
1(1):33–47. 461

Wei Chen, Zhen Huang, Liang Xie, Binbin Lin, 462  
Houqiang Li, Le Lu, Xinmei Tian, Deng Cai, 463  
Yonggang Zhang, Wenxiao Wang, Xu Shen, and 464  
Jieping Ye. 2025. From Yes-Men to Truth- 465  
Tellers: Addressing Sycophancy in Large Language 466  
Models with Pinpoint Tuning. *arXiv preprint*. 467  
ArXiv:2409.01658. 468

Vanessa Choy, Sara Martin, and Ashley Lumpkin. 469  
2024. Can we rely on generative AI for healthcare 470  
information? Publisher: Ipsos. 471

Justin Cui, Wei-Lin Chiang, Ion Stoica, and Cho-Jui 472  
Hsieh. 2025. OR-Bench: An Over-Refusal Bench- 473  
mark for Large Language Models. *arXiv preprint*. 474  
ArXiv:2405.20947. 475

Emily R. Doherty-Torstrick, Kate E. Walton, and 476  
Brian A. Fallon. 2016. Cyberchondria: Parsing 477  
Health Anxiety From Online Behavior. *Psychoso- 478  
matics*, 57(4):390–400. 479

Charles A. Dorison and 1 others. 2022. In COVID-19 480  
Health Messaging, Loss Framing Increases Anxiety 481  
with Little-to-No Concomitant Benefits: Experimen- 482  
tal Evidence from 84 Countries. *Affective Science*, 483  
3(3):577–602. 484

L. Fernández de la Cruz, M. Rydell, B. Runeson, B. M. 485  
D’Onofrio, G. Brander, C. Rück, P. Lichtenstein, 486  
H. Larsson, and D. Mataix-Cols. 2017. Suicide in 487  
obsessive-compulsive disorder: a population-based 488  
study of 36788 Swedish patients. *Molecular Psychi- 489  
atry*, 22(11):1626–1632. 490

Lorena Fernández de la Cruz, Kayoko Isomura, Paul 491  
Lichtenstein, Christian Rück, and David Mataix- 492  
Cols. 2022. Morbidity and mortality in obsessive- 493  
compulsive disorder: A narrative review. *Neuro- 494  
science & Biobehavioral Reviews*, 136:104602. 495

Gabriela M. Ferreira, Natalie V. Zanini, Gabriela B. 496  
De Menezes, Lucy Albertella, Louise Destree, and 497  
Leonardo F. Fontenelle. 2018. When patients with 498  
OCD decide to seek, and not to avoid harm: The 499  
problem of suicidality in OCD. *Bulletin of the Men- 500  
ninger Clinic*, 82(4):360–374. 501

Bernard Fitzgerald. 2025. Introducing Over- 502  
Alignment. 503

Jon E. Grant, Lynne Drummond, Timothy R. Nichol- 504  
son, Harry Fagan, David S. Baldwin, Naomi A. 505  
Fineberg, and Samuel R. Chamberlain. 2022. 506  
Obsessive-compulsive symptoms and the Covid-19 507

{5}------------------------------------------------

|  |  |  |
|-|-|-|
| 508 | pandemic: A rapid scoping review. <i>Neuroscience &amp;</i> | 562 |
| 509 | <i>Biobehavioral Reviews</i> , 132:1086–1098. | 563 |
| 510 | Dan Hendrycks, Collin Burns, Steven Basart, Andrew | 564 |
| 511 | Critch, Jerry Li, Dawn Song, and Jacob Steinhardt. | 565 |
| 512 | 2023. <i>Aligning AI With Shared Human Values.</i> | 566 |
| 513 | <i>arXiv preprint</i> . ArXiv:2008.02275. | 567 |
| 514 | Yeonjun In, Wonjoong Kim, Kanghoon Yoon, | 568 |
| 515 | Sungchul Kim, Mehrab Tanjim, Kibum Kim, and | 569 |
| 516 | Chanyoung Park. 2025. <i>Is Safety Standard Same</i> | 570 |
| 517 | <i>for Everyone? User-Specific Safety Evaluation</i> |  |
| 518 | <i>of Large Language Models. arXiv preprint.</i> |  |
| 519 | ArXiv:2502.15086. |  |
| 520 | International OCD Foundation. <i>OCD and Contamina-</i> |  |
| 521 | <i>tion.</i> |  |
| 522 | LYNNE M. Drummond, AZMATTHULLA |  |
| 523 | KHAM HAMEED, and RUXANDRA ION. |  |
| 524 | 2011. <i>Physical complications of severe enduring</i> |  |
| 525 | <i>obsessive-compulsive disorder. World Psychiatry</i> , |  |
| 526 | 10(2):154. |  |
| 527 | Simon Mack, Frank Jacobi, Anja Gerschler, Jens |  |
| 528 | Strehle, Michael Höfler, Markus A. Busch, Ulrike E. |  |
| 529 | Maske, Ulfert Hapke, Ingeburg Seiffert, Wolfgang |  |
| 530 | Gaebel, Jürgen Zielasek, Wolfgang Maier, and Hans- |  |
| 531 | Ulrich Wittchen. 2014. <i>Self-reported utilization of</i> |  |
| 532 | <i>mental health services in the adult German popu-</i> |  |
| 533 | <i>lation – evidence for unmet needs? Results of the</i> |  |
| 534 | <i>DEGS1-Mental Health Module (DEGS1-MH). In-</i> |  |
| 535 | <i>ternational Journal of Methods in Psychiatric Re-</i> |  |
| 536 | <i>search</i> , 23(3):289–303. |  |
| 537 | Mayo Clinic. <i>Obsessive-compulsive disorder (OCD) -</i> |  |
| 538 | <i>Symptoms and causes.</i> |  |
| 539 | Sandra M. Meier, Manuel Matthiesen, Ole Mors, Di- |  |
| 540 | ana E. Schendel, Preben B. Mortensen, and Ker- |  |
| 541 | stin J. Plessen. 2016. <i>Mortality Among Persons</i> |  |
| 542 | <i>With Obsessive-Compulsive Disorder in Denmark.</i> |  |
| 543 | <i>JAMA psychiatry</i> , 73(3):268–274. |  |
| 544 | Denelle Mohammed, Sara Wilcox, Camille Renee, |  |
| 545 | Christine Janke, Niki Jarrett, Anjelika Evangelopou- |  |
| 546 | los, Chasity Serrano, Nazmin Tabassum, Natasha |  |
| 547 | Turner, Melody Theodore, Aleksandar Dusic, and |  |
| 548 | Rana Zeine. 2019. <i>Cyberchondria: Implications of</i> |  |
| 549 | <i>online behavior and health anxiety as determinants.</i> |  |
| 550 | <i>Archives of Medicine and Health Sciences</i> , 7(2):154. |  |
| 551 | Regina Müller, Malte Klemmt, Roland Koch, Hans- |  |
| 552 | Jörg Ehni, Tanja Henking, Elisabeth Langmann, Ur- |  |
| 553 | ban Wiesing, and Robert Ranisch. 2024. “That’s just |  |
| 554 | <i>Future Medicine” – a qualitative study on users’ ex-</i> |  |
| 555 | <i>periences of symptom checker apps. BMC Medical</i> |  |
| 556 | <i>Ethics</i> , 25(1):17. |  |
| 557 | Simon Münker. 2025. <i>Cultural Bias in Large Language</i> |  |
| 558 | <i>Models: Evaluating AI Agents through Moral Ques-</i> |  |
| 559 | <i>tionnaires. arXiv preprint</i> . ArXiv:2507.10073. |  |
| 560 | Open AI. 2025. <i>Sycophancy in GPT-4o: What hap-</i> |  |
| 561 | <i>pened and what we’re doing about it.</i> |  |
| Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, |  | 562 |
| Carroll L. Wainwright, Pamela Mishkin, Chong |  | 563 |
| Zhang, Sandhini Agarwal, Katarina Slama, Alex |  | 564 |
| Ray, John Schulman, Jacob Hilton, Fraser Kelton, |  | 565 |
| Luke Miller, Maddie Simens, Amanda Askell, |  | 566 |
| Peter Welinder, Paul Christiano, Jan Leike, and Ryan |  | 567 |
| Lowe. 2022. <i>Training language models to follow</i> |  | 568 |
| <i>instructions with human feedback. arXiv preprint.</i> |  | 569 |
| ArXiv:2203.02155. |  | 570 |
| Shumiao Ouyang, Hayong Yun, and Xingjian Zheng. |  | 571 |
| 2025. <i>AI as Decision-Maker: Ethics and</i> |  | 572 |
| <i>Risk Preferences of LLMs. arXiv preprint.</i> |  | 573 |
| ArXiv:2406.01168. |  | 574 |
| Ruchira Ray and Ruchi Bhalani. 2024. <i>Mitigating Ex-</i> |  | 575 |
| <i>aggerated Safety in Large Language Models. arXiv</i> |  | 576 |
| <i>preprint</i> . ArXiv:2405.05418. |  | 577 |
| Robin Segerer. 2025. <i>Cultural Value Alignment in</i> |  | 578 |
| <i>Large Language Models: A Prompt-based Analy-</i> |  | 579 |
| <i>sis of Schwartz Values in Gemini, ChatGPT, and</i> |  | 580 |
| <i>DeepSeek. arXiv preprint</i> . ArXiv:2505.17112. |  | 581 |
| Mrinank Sharma, Meg Tong, Tomasz Korbak, David |  | 582 |
| Duvenaud, Amanda Askell, Samuel R. Bow- |  | 583 |
| man, Newton Cheng, Esin Durmus, Zac Hatfield- |  | 584 |
| Dodds, Scott R. Johnston, Shauna Kravec, Timothy |  | 585 |
| Maxwell, Sam McCandlish, Kamal Ndousse, Oliver |  | 586 |
| Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, |  | 587 |
| and Ethan Perez. 2025. <i>Towards Understanding</i> |  | 588 |
| <i>Sycophancy in Language Models. arXiv preprint.</i> |  | 589 |
| ArXiv:2310.13548. |  | 590 |
| Huda A. Sherif, Khaled Tawfeeq, Zahraa Mohamed, |  | 591 |
| Lobna Abdelhakeem, Sara H. Tahoon, Mahasen |  | 592 |
| Mosa, Karima Samy, Karema Hamdy, Lamiaa El- |  | 593 |
| lakwa, and Salma Elnoamy. 2023. “Medical stu- |  | 594 |
| dent syndrome”: a real disease or just a myth?—a |  | 595 |
| cross-sectional study at Menoufia University, Egypt. |  | 596 |
| <i>Middle East Current Psychiatry, Ain Shams Univer-</i> |  | 597 |
| <i>sity</i> , 30(1):42. |  | 598 |
| Margit Sutrop. 2020. <i>Challenges of Aligning Artificial</i> |  | 599 |
| <i>Intelligence with Human Values. Acta Baltica His-</i> |  | 600 |
| <i>toriae et Philosophiae Scientiarum</i> , 8(2):54–72. |  | 601 |
| Team Qwen. 2025. <i>Qwen3-Coder: Agentic Coding in</i> |  | 602 |
| <i>the World.</i> |  | 603 |
| Alexey Turchin. 2019. <i>AI alignment problem: Human</i> |  | 604 |
| <i>values don’t actually exist.</i> |  | 605 |
| Anna-Jasmin Wetzel, Malte Klemmt, Regina Müller, |  | 606 |
| Monika A. Rieger, Stefanie Joos, and Roland Koch. |  | 607 |
| 2024. <i>Only the anxious ones? Identifying char-</i> |  | 608 |
| <i>acteristics of symptom checker app users: a cross-</i> |  | 609 |
| <i>sectional survey. BMC Medical Informatics and De-</i> |  | 610 |
| <i>cision Making</i> , 24(1):21. |  | 611 |
| Lionel Wong, Ayman Ali, Raymond Xiong, Shan- |  | 612 |
| non Zeijang Shen, Yoon Kim, and Monica Agrawal. |  | 613 |
| 2025. <i>Retrieval-augmented systems can be dan-</i> |  | 614 |
| <i>gerous medical communicators. arXiv preprint.</i> |  | 615 |
| ArXiv:2502.14898. |  | 616 |

{6}------------------------------------------------

617 Qianqian Xie, Qingyu Chen, Aokun Chen, Cheng 674  
618 Peng, Yan Hu, Fongci Lin, Xueqing Peng, Jimin 675  
619 Huang, Jeffrey Zhang, Vipina Keloth, Xinyu Zhou, 676  
620 Lingfei Qian, Huan He, Dennis Shung, Lucila Ohno- 677  
621 Machado, Yonghui Wu, Hua Xu, and Jiang Bian. 678  
622 2024. *Me LLaMA: Foundation Large Language*  
623 *Models for Medical Applications. arXiv preprint.*  
624 *ArXiv:2402.12749.*

625 Yifan Zeng, Liang Kairong, Fangzhou Dong, and 679  
626 Peijia Zheng. 2025. *Quantifying Risk Propensi-*  
627 *ties of Large Language Models: Ethical Focus and*  
628 *Bias Detection through Role-Play. arXiv preprint.*  
629 *ArXiv:2411.08884.*

630 Sina Ziegler, Klara Bednasch, Sabrina Baldofski, and 680  
631 Christine Rummel-Kluge. 2021. *Long durations*  
632 *from symptom onset to diagnosis and from diag-*  
633 *nosis to treatment in obsessive-compulsive disor-*  
634 *der: A retrospective self-report study. PLOS ONE,*  
635 *16(12):e0261169.*

###### 636 A Detailed related work on AI alignment

###### 637 A.1 LLM Alignment and Value Pluralism

638 AI developers often claim that they have aligned their 674  
639 AI with “human values” or “human preferences”, aim- 675  
640 ing to increase its usefulness and harmlessness, in- 676  
641 cluding InsturctGPT and Anthropic AI.(Ouyang et al., 677  
642 2022; Bai et al., 2022; Hendrycks et al., 2023). One 678  
643 such value or preference is safety. However, even 679  
644 something as seemingly universal as safety looks dif- 680  
645 ferent in different places to different people. Sutrop 681  
646 (2020) concerns that AI developers underestimated the 682  
647 difficulty of the question about which values or whose 683  
648 values the AI should align with. The authors argued 684  
649 that given that our everyday life is full of moral dis- 685  
650 agreements and the plural nature of values, how can 686  
651 we decide which objectives or values we inject into the 687  
652 AIs? *Arzberger et al. (2024)* argues that current align- 688  
653 ment approaches rely on universal framings of human 689  
654 values, which could be problematic and result in AI 690  
655 systems that are biased, leading to equity and justice 691  
656 issues. *Turchin (2019)* proposed an even more crit- 692  
657 ical point of view, which argues that “human values” 693  
658 are not an object, “human value system” has flaws, 694  
659 and even “human values” are not good by default. He 695  
660 suggests that “human values” in AI should be replaced 696  
661 with something better, or at least used very cautiously. 697  
662 Existing evaluations have shown that the model could 698  
663 be biased towards different cultural backgrounds, due 699  
664 to either unintentional bias in the training data or in- 700  
665 tentional bias introduced during alignment. *Seegerer* 701  
666 *(2025)* finds that DeepSeek (a Chinese LLM) shows 702  
667 more value towards collectivism compared to Western 703  
668 LLMs. *Münker (2025)* states that their study sug- 704  
669 gests a concerning reality: “Large Language Models 705  
670 (LLMs) fail to represent diverse cultural moral frame- 706  
671 works despite their linguistic capabilities.” They high- 707  
672 lighted the need for culturally-informed alignment ob- 708  
673 jectives. Current approach regresses the model to a 709

“mean moral framework” rather than representing di- 674  
verse human values. Without cross-cultural evaluation 675  
metrics, models may appear well-aligned within the 676  
tested context but fail to perform appropriately under 677  
alternative moral frameworks. 678

The term over-alignment has been used informally 679  
before to describe how “AI systems excessively rely 680  
on a user’s expertise, perceptions, or hypotheses with- 681  
out sufficient independent validation or critical engage- 682  
ment” (*Fitzgerald, 2025*). This problem is also some- 683  
times referred to as “AI sycophant” (*Open AI, 2025*; 684  
*Sharma et al., 2025*; *Chen et al., 2025*; *Arvin, 2025*). It 685  
describes where AI is over-aligned on “helpfulness” or 686  
“friendliness”, and thus cannot give meaningful advice. 687  
This is different to what we are describing in this pa- 688  
per, which tackle the problems that AI is over-aligned 689  
to “harmlessness.” 690

A large body of literature examines LLMs’ approach 691  
to risk. *Ouyang et al. (2025)* studied how LLMs’ 692  
cautiousness in ethical alignment affects economically 693  
valuable risk-taking, which might affect economic 694  
forecasts and suppress valuable risk-taking. *Zeng et al.* 695  
*(2025)* applied DOSPERT (*Blais and Weber, 2006*) to 696  
different LLMs and found that they show different risk 697  
tolerance in different areas; however, they did not com- 698  
pare with a human baseline. *Ray and Bhalani (2024)* 699  
studied LLMs’ over-refusal in cases like prompts with 700  
homonyms (e.g., how to kill a process) or safe context 701  
(“how to kill someone in [a video game name]”), etc. 702  
They found that many LLMs have problems with over- 703  
refusing prompts. *Cui et al. (2025)* is another bench- 704  
mark and evaluation for model over-refusal, and they 705  
found a positive relationship between over-refusal and 706  
safety. *In et al. (2025)* argued that AI safety should be 707  
tailored to individual people. For example, a normal 708  
diet question might be harmless for normal people, but 709  
be dangerous for people with an eating disorder. How- 710  
ever, this work only focuses on how AI should be more 711  
“cautious” for certain populations, instead of avoid- 712  
ing being overly cautious. Although we agree with 713  
their idea that AI safety is contextual, we do not model 714  
this problem as a personalized AI problem, as (1) we 715  
strongly disagree with giving a person’s mental health, 716  
criminal, and financial details to AI and AI providers, 717  
which raises significant privacy, anonymity, and auton- 718  
omy concerns; and (2) we argue that AI should be con- 719  
text aware and avoid being overly cautious in any situ- 720  
ations, regardless user’s mental health history. 721

###### 722 B Potential Solutions

The overalignment problem arises from two pri- 723  
mary sources: alignment processes that overempha- 724  
size safety at the expense of reasonability, and tech- 725  
nical limitations that lead developers to implement ex- 726  
cessive caution as a compensatory measure. This phe- 727  
nomenon parallels ROC curve optimization, where sys- 728  
tems with limited discriminative ability (low area under 729  
the curve) require conservative thresholds to minimize 730

{7}------------------------------------------------

731 false negatives, inevitably increasing false positives.  
732 When AI systems lack sufficient reasoning capabilities,  
733 developers might make the AI lean toward overly cau-  
734 tious responses to prevent harmful under-cautious out-  
735 puts.

736 While we acknowledge these underlying causes, we  
737 contend that overalignment remains problematic and  
738 ethically concerning regardless of its origins. How-  
739 ever, our goal is not to advocate for under-cautious  
740 AI systems. Instead, we propose solutions that re-  
741 duce over-cautious responses while maintaining app-  
742 ropriate safety standards through enhanced AI capabil-  
743 ities in reasoning, contextual understanding, and nu-  
744 anced decision-making.

745 **Domain-Specific Model Development.** For criti-  
746 cal domains such as healthcare, developing specialized  
747 fine-tuned models may prove beneficial. These models  
748 could focus specifically on improving domain-relevant  
749 knowledge and reasoning capabilities, similar to exist-  
750 ing specialized coding models like Qwen Coder (Team  
751 Qwen, 2025). There are some existing models like  
752 MeLLaMA (Xie et al., 2024), but they are not widely  
753 used and consumer-accessible.

754 However, this might prompt more people to use  
755 these LLMs for health information, which might not  
756 be helpful (or even risky) until these models are good  
757 enough. Therefore, we recommend initiating research  
758 on such specialized models while not promoting them  
759 as a better model until comprehensive safety evalua-  
760 tions demonstrate their readiness for general use. Al-  
761 ternatively, a routing mechanism can route medical-  
762 related questions to special models behind the scenes,  
763 which will improve the model’s health-related reason-  
764 ing abilities without promoting it as a model finetuned  
765 for health.

766 **Professionals in Alignment.** We can include more  
767 health professionals in the alignment, designing spe-  
768 cific training datasets, and when evaluating, focus on  
769 both over- and under-cautious. HealthBench (Arora  
770 et al., 2025) has already addressed that emergency  
771 triage mistakes, both over- and underdiagnosis, could  
772 be harmful.

773 **User and Public Education.** Users and the public  
774 should be educated that they need better awareness of  
775 the limits of AI for health information, similar to what  
776 happened with online searches. They should know that  
777 overly cautious answers can worsen health anxiety or  
778 OCD. Public awareness of OCD and anxiety should be  
779 increased and be encouraged to seek professional men-  
780 tal health help if such signs appear, given the long de-  
781 lays in diagnosis.

 Rest of paper (reference and Appendix) is removed.