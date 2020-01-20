% Estimate RSA Distances with Noise

% Generate Distance Estimates:
clear
s = [.2:.05:5]; i=1; up=logical(tril(ones(100),-1));
for ss = s
    X = ss*randn(100,20);
    noise = randn(100,20);
    
    td_eu = (pdist(X, 'euclidean'));
    ed_eu = (pdist(X+noise, 'euclidean')); 
    R_eu(i) = mean(ed_eu./td_eu);
    
    td_sq = (pdist(X, 'seuclidean'));
    ed_sq = (pdist(X+noise, 'seuclidean'));
    R_sq(i) = mean(ed_sq./td_sq);
    
    td_ma = (pdist(X, 'mahalanobis'));
    ed_ma = (pdist(X+noise, 'mahalanobis')); 
    R_ma(i) = mean(ed_ma./td_ma);
    
    td_co = (pdist(X, 'cosine'));
    ed_co = (pdist(X+noise, 'cosine')); 
    R_co(i) = mean(ed_co./td_co);
    
    td_cr = (pdist(X, 'correlation'));
    ed_cr = (pdist(X+noise, 'correlation')); 
    R_cr(i) = mean(ed_cr./td_cr);
    
    td_sp = (pdist(X, 'spearman'));
    ed_sp = (pdist(X+noise, 'spearman'));
    R_sp(i) = mean(ed_sp./td_sp);
    
    s1 = X+noise; s2 = X+randn(100,20);
    s1 = s1*(cov(s1)^(-1/2)); s2 = s2*(cov(s2)^(-1/2));
    for j=1:100
        for k=1:100
            d(j,k) = sqrt((s1(j,:)-s1(k,:))*(s2(j,:)-s2(k,:))');
        end
    end
    ed_cma = real(d(up));
    R_cma(i) = mean(ed_cma'./td_ma);
    
    i=i+1;
end

hold on
scatter(s,R_eu,'filled')
scatter(s,R_sq,'filled')
scatter(s,R_ma,'filled')
scatter(s,R_co,'filled')
scatter(s,R_cr,'filled')
scatter(s,R_sp,'filled')
scatter(s,R_cma,'filled')
legend('Euclidean','Standardized Euclidean','Mahalanobis','Cosine','Correlation','Spearman','Cross-Validated Mahalanobis')
hold off

% Mantel Test With Noise
clear
s = [.2:.05:10]; i=1;up=logical(tril(ones(100),-1));
for ss = s
    X = ss*rand(100,20);
    varS(i) = var(X(:));
    noise1 = (randn(100,20));
    noise2 = (randn(100,20));
    
    td_eu = pdist(X, 'euclidean');
    ed_eu = pdist(X+noise2, 'euclidean'); 
    Reu(i) = mantel(td_eu,ed_eu);
    
    td_sq = pdist(X, 'seuclidean');
    ed_sq = pdist(X+noise2, 'seuclidean');
    Rsq(i) = mantel(td_sq,ed_sq);
    
    td_ma = pdist(X, 'mahalanobis');
    ed_ma = pdist(X+noise2, 'mahalanobis'); 
    Rma(i) = mantel(td_ma,ed_ma); 
    
    td_co = pdist(X, 'cosine');
    ed_co = pdist(X+noise2, 'cosine'); 
    Rco(i) = mantel(td_sq, ed_sq); 
    
    td_cr = pdist(X, 'correlation');
    ed_cr = pdist(X+noise2, 'correlation'); 
    Rcr(i) = mantel(td_cr,ed_cr);
    
    td_sp = pdist(X, 'spearman');
    ed_sp = pdist(X+noise2, 'spearman');
    Rsp(i) = mantel(td_sp,ed_sp); 
    
    s1 = X+noise1; s2 = X+noise2;
    s1 = s1*(cov(s1)^(-1/2)); s2 = s2*(cov(s2)^(-1/2));
    for j=1:100
        for k=1:100
            d(j,k) = sqrt((s1(j,:)-s1(k,:))*(s2(j,:)-s2(k,:))');
        end
    end
    ed_cma = real(d(up));
    Rcma(i) = mantel(td_ma,ed_cma');
    
    s1 = X+noise1; s2 = X+noise2;
    for j=1:100
        for k=1:100
            d(j,k) = sqrt(norm(s1(j,:)-s1(k,:))*norm(s2(j,:)-s2(k,:)));
        end
    end
    ed_ceu = real(d(up));
    Rceu(i) = mantel(td_eu, ed_ceu');
    
    i=i+1;
end
hold on
scatter(varS,Reu,'filled')
scatter(varS,Rsq,'filled')
scatter(varS,Rma,'filled')
scatter(varS,Rco,'filled')
scatter(varS,Rcr,'filled')
scatter(varS,Rsp,'filled')
scatter(varS,Rcma,'filled')
scatter(varS,Rceu,'filled')
legend('Euclidean','Standardized Euclidean','Mahalanobis','Cosine','Correlation','Spearman','Cross-Validated Mahalanobis','Cross-Validated Euclidean')
hold off

% Note, standardized eurclidean is same as cosine for our toy example
