-- ST-01 スタッフの新規登録
insert INTO mst_staff VALUES (
    "staff@staff.com","password","スタッフ太郎"
);

-- CT-01 会員の新規登録
insert INTO mst_customer VALUES (
    "test@test.com", "password", "テスト太郎", null, null, null, 0
);

-- CT-02 会員の新規登録 2回目
insert INTO mst_customer VALUES (
    "test@test.com", "password", "テスト太郎", null, null, null, 0
);

-- EC-01 イベントカテゴリ新規登録
insert into mst_event_category VALUES (
    "イベントカテゴリ"
);

-- ET-01 イベント新規登録
insert into mst_event VALUES (
    1, 1, '大運動会', '2022/04/25', '東京', 'これは大運動会です。'
);

-- TI-01 チケット新規登録
insert into mst_ticket VALUES (
    1, "s01", 1, 1
);

-- RV-01 予約情報新規登録
insert into tbl_reservation VALUES (
    1, 1
);

-- イベント新規登録
-- ET-02 - ET-21
insert into mst_event VALUES (2, 1, '大コンサート', '2022/04/26', '埼玉', 'これは大コンサートです。');
insert into mst_event VALUES (3, 1, '大花火大会', '2022/04/27', '群馬', 'これは大花火大会です。');
insert into mst_event VALUES (4, 1, '大音楽祭', '2022/04/28', '東京', 'これは大音楽祭です。');
insert into mst_event VALUES (1, 5, '大感謝祭', '2022/04/29', '東京', 'これは大感謝祭です。');
insert into mst_event VALUES (6, 1, '大葉祭', '2022/05/25', '東京', 'これは大葉祭です。');
insert into mst_event VALUES (7, 1, '大ゲーム大会', '2022/06/25', '東京', 'これは大ゲーム大会です。');
insert into mst_event VALUES (8, 1, '大海水浴', '2022/07/25', '東京', 'これは大海水浴です。');
insert into mst_event VALUES (9, 1, '大かき氷祭り', '2022/08/25', '東京', 'これは大かき氷祭りです。');
insert into mst_event VALUES (10, 1, '大紅葉狩り', '2022/09/25', '東京', 'これは大紅葉狩りです。');
insert into mst_event VALUES (11, 1, '大パン祭り', '2024/07/25', '東京', 'これは大パン祭りです。');
insert into mst_event VALUES (12, 1, '大歌舞伎揚げ', '2024/08/25', '東京', 'これは大歌舞伎揚げです。');
insert into mst_event VALUES (13, 1, '大ダンス大会', '2024/09/25', '東京', 'これは大ダンス大会です。');
insert into mst_event VALUES (14, 1, '大クラシックコンサート', '2024/10/25', '東京', 'これは大クラシックコンサートです。');
insert into mst_event VALUES (15, 1, '大ボーリング大会', '2024/11/25', '東京', 'これは大ボーリング大会です。');
insert into mst_event VALUES (16, 1, '大クリスマスコンサート', '2024/12/25', '沖縄', 'これは大クリスマスコンサートです。');
insert into mst_event VALUES (17, 1, '大七草粥イベント', '2025/01/25', '東京', 'これは大七草粥イベントです。');
insert into mst_event VALUES (18, 1, '大HIPPOPライブ', '2025/02/25', '東京', 'これは大HIPPOPライブです。');
insert into mst_event VALUES (19, 1, '大アートイベント', '2025/03/25', '東京', 'これは大アートイベントです。');
insert into mst_event VALUES (20, 1, '大演劇', '2025/04/25', '東京', 'これは大演劇です。');
insert into mst_event VALUES (21, 1, '大呪物展', '2025/05/25', '東京', 'これは大呪物展です。');
