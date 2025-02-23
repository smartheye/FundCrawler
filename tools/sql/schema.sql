-- public.t_public_fund_real_time definition

-- Drop table

-- DROP TABLE public.t_public_fund_real_time;

CREATE TABLE t_public_fund_real_time (
	optime timestamptz NOT NULL,
	public_fund_symbol bpchar(6) NOT NULL,
	public_fund_name bpchar,
	public_fund_name_pinyin bpchar,
	latest_nav_text bpchar,
    latest_nav DOUBLE PRECISION,
	latest_cumulative_nav_text bpchar,
    latest_cumulative_nav DOUBLE PRECISION,
	historical_nav_text bpchar,
    historical_nav DOUBLE PRECISION,
	historical_cumulative_nav_text bpchar,
	historical_cumulative_nav DOUBLE PRECISION,
	daily_growth_value_text bpchar,
    daily_growth_value DOUBLE PRECISION,
	daily_growth_rate_text bpchar,
    daily_growth_rate DOUBLE PRECISION,
	subscription_status bpchar,
	redemption_status bpchar,
    CONSTRAINT t_public_fund_real_time_pk PRIMARY KEY (optime, public_fund_symbol)
);

COMMENT ON TABLE  t_public_fund_real_time        IS '公募基金实时净值';
COMMENT ON COLUMN t_public_fund_real_time.optime IS '数据收集时间';
COMMENT ON COLUMN t_public_fund_real_time.public_fund_symbol IS '公募基金代号。6位数字';
COMMENT ON COLUMN t_public_fund_real_time.public_fund_name IS '基金简称';
COMMENT ON COLUMN t_public_fund_real_time.public_fund_name_pinyin IS '基金简称拼音';
COMMENT ON COLUMN t_public_fund_real_time.latest_nav_text IS '最新单位净值(latest net asset value)';
COMMENT ON COLUMN t_public_fund_real_time.latest_nav IS '最新单位净值(latest net asset value)';
COMMENT ON COLUMN t_public_fund_real_time.latest_cumulative_nav_text IS '最新累计净值（latest cumulative net asset value)';
COMMENT ON COLUMN t_public_fund_real_time.latest_cumulative_nav IS '最新累计净值（latest cumulative net asset value)';
COMMENT ON COLUMN t_public_fund_real_time.historical_nav_text IS '历史单位净值（historical net asset value）';
COMMENT ON COLUMN t_public_fund_real_time.historical_nav IS '历史单位净值（historical net asset value）';
COMMENT ON COLUMN t_public_fund_real_time.historical_cumulative_nav_text IS '历史累计净值（historical cumulative net asset value）';
COMMENT ON COLUMN t_public_fund_real_time.historical_cumulative_nav IS '历史累计净值（historical cumulative net asset value）';
COMMENT ON COLUMN t_public_fund_real_time.daily_growth_value_text IS '日增长值';
COMMENT ON COLUMN t_public_fund_real_time.daily_growth_value IS '日增长值';
COMMENT ON COLUMN t_public_fund_real_time.daily_growth_rate_text IS '日增长率';
COMMENT ON COLUMN t_public_fund_real_time.daily_growth_rate IS '日增长率';
COMMENT ON COLUMN t_public_fund_real_time.subscription_status IS '申购状态';
COMMENT ON COLUMN t_public_fund_real_time.redemption_status IS '赎回状态';