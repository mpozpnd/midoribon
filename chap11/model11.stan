data {
   int<lower=1> N;
   int<lower=0> Y[N];
}

parameters {
   real r[N];
   real<lower=0> s_r;
}

model {
   for (j in 2:N)
      r[j] ~ normal(r[j-1], s_r);
   for (j in 1:N)
      Y[j] ~ poisson_log(r[j]);
}

generated quantities {
   real<lower=0> Y_mean[N];
   for (j in 1:N)
      Y_mean[j] <- exp(r[j]);
}
