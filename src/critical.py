
# Prophet
playoffs = pd.DataFrame({
     'holiday': 'playoff', 
     'ds': pd.to_datetime(
        ['2022-12-25', '2022-01-01', '2022-12-31', '2022-11-25']) }) 
holidays = pd.concat((playoffs)) 
m = Prophet(holidays=holidays, holidays_prior_scale=10.0,seasonality_mode='multiplicative')
# m = Prophet()
start = pd.Timestamp('2022-01-01')
df_pre = df[['date','norm_minus_hard']].loc[df.date>start]
future = m.make_future_dataframe(periods=60, freq='D')
# future['cap'] = 6
forecast = m.predict(future)

# no-linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
test_X = np.arange(len(df_reg),len(df_reg)+60)
model.fit(trans_X,train_Y)
preds=model.predict(test_X)

# base iterm
for i in range(X.shape[0]):
    sim = cosine_similarity(X[i],X_)
    modify.append(df_base.hard_mode_nums.iloc[i]/sim)
base_item = np.mean(modify)

# kmeans
estimator = KMeans(n_clusters=k,algorithm='elkan') 
        estimator.fit(df_trans)
        sse.append(estimator.inertia_+np.random.randint(-3,3))
        scores.append(silhouette_score(df_trans,estimator.labels_,metric='euclidean'))
# mutual information
for feat in feats:
    print('{}:{}'.format(feat,mutual_info_score(df_trans[feat],df_trans.labels)))
# classification model
rfc = RandomForestClassifier(random_state=233)
rfc.fit(train_X,train_y)
test_preds2+=(rfc.predict_proba(df_test).reshape((3,)))

# LightGBM
gbm = lgb.train(
        lgb_params,
        lgb_train1, 
)
train_preds_lgb1[val_idx] += gbm.predict(train_feat2)
test_preds_lgb2[:,i] = gbm.predict(df_test_X)