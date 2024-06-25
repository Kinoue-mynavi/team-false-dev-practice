-- ST-01 スタッフの新規登録
insert INTO mst_staff VALUES (
    1, "staff@staff.com","password","スタッフ太郎"
);

-- CT-01 会員の新規登録
insert INTO mst_customer VALUES (
    1, "test@test.com", "password", "テスト太郎", null, null, null, 0
);

-- CT-02 会員の新規登録 2回目
insert INTO mst_customer VALUES (
    2, "test@test.com", "password", "テスト太郎", null, null, null, 0
);

-- EC-01 イベントカテゴリ新規登録
insert into mst_event_category VALUES (
    1, "イベントカテゴリ"
);

-- ET-01 イベント新規登録
insert into mst_event VALUES (
    1, 1, '大運動会', '2022-04-25', '東京', 'これは大運動会です。'
);

-- ET-02 - ET-21
insert into mst_event VALUES (2, 1, '大コンサート', '2022-04-26', '埼玉', 'これは大コンサートです。');
insert into mst_event VALUES (3, 1, '大花火大会', '2022-04-27', '群馬', 'これは大花火大会です。');
insert into mst_event VALUES (4, 1, '大音楽祭', '2022-04-28', '東京', 'これは大音楽祭です。');
insert into mst_event VALUES (5, 1, '大感謝祭', '2022-04-29', '東京', 'これは大感謝祭です。');
insert into mst_event VALUES (6, 1, '大葉祭', '2022-05-25', '東京', 'これは大葉祭です。');
insert into mst_event VALUES (7, 1, '大ゲーム大会', '2022-06-25', '東京', 'これは大ゲーム大会です。');
insert into mst_event VALUES (8, 1, '大海水浴', '2022-07-25', '東京', 'これは大海水浴です。');
insert into mst_event VALUES (9, 1, '大かき氷祭り', '2022-08-25', '東京', 'これは大かき氷祭りです。');
insert into mst_event VALUES (10, 1, '大紅葉狩り', '2022-09-25', '東京', 'これは大紅葉狩りです。');
insert into mst_event VALUES (11, 1, '大パン祭り', '2024-07-25', '東京', 'これは大パン祭りです。');
insert into mst_event VALUES (12, 1, '大歌舞伎揚げ', '2024-08-25', '東京', 'これは大歌舞伎揚げです。');
insert into mst_event VALUES (13, 1, '大ダンス大会', '2024-09-25', '東京', 'これは大ダンス大会です。');
insert into mst_event VALUES (14, 1, '大クラシックコンサート', '2024-10-25', '東京', 'これは大クラシックコンサートです。');
insert into mst_event VALUES (15, 1, '大ボーリング大会', '2024-11-25', '東京', 'これは大ボーリング大会です。');
insert into mst_event VALUES (16, 1, '大クリスマスコンサート', '2024-12-25', '沖縄', 'これは大クリスマスコンサートです。');
insert into mst_event VALUES (17, 1, '大七草粥イベント', '2025-01-25', '東京', 'これは大七草粥イベントです。');
insert into mst_event VALUES (18, 1, '大HIPPOPライブ', '2025-02-25', '東京', 'これは大HIPPOPライブです。');
insert into mst_event VALUES (19, 1, '大アートイベント', '2025-03-25', '東京', 'これは大アートイベントです。');
insert into mst_event VALUES (20, 1, '大演劇', '2025-04-25', '東京', 'これは大演劇です。');
insert into mst_event VALUES (21, 1, '大呪物展', '2025-05-25', '東京', 'これは大呪物展です。');

-- TI-01 チケット新規登録
insert into mst_ticket VALUES (
    1, 1, "s01", 1, 1
);

-- TI-02 - TI-21
insert into mst_ticket VALUES (2, 2, "s01", 2, 1);
insert into mst_ticket VALUES (3, 3, "s01", 3, 1);
insert into mst_ticket VALUES (4, 4, "s01", 4, 1);
insert into mst_ticket VALUES (5, 5, "s01", 5, 1);
insert into mst_ticket VALUES (6, 6, "s01", 6, 1);
insert into mst_ticket VALUES (7, 7, "s01", 7, 1);
insert into mst_ticket VALUES (8, 8, "s01", 8, 1);
insert into mst_ticket VALUES (9, 9, "s01", 9, 1);
insert into mst_ticket VALUES (10, 10, "s01", 10, 1);
insert into mst_ticket VALUES (11, 11, "s01", 11, 1);
insert into mst_ticket VALUES (12, 12, "s01", 12, 1);
insert into mst_ticket VALUES (13, 13, "s01", 13, 1);
insert into mst_ticket VALUES (14, 14, "s01", 14, 1);
insert into mst_ticket VALUES (15, 15, "s01", 15, 1);
insert into mst_ticket VALUES (16, 16, "s01", 16, 1);
insert into mst_ticket VALUES (17, 17, "s01", 17, 1);
insert into mst_ticket VALUES (18, 18, "s01", 18, 1);
insert into mst_ticket VALUES (19, 19, "s01", 19, 1);
insert into mst_ticket VALUES (20, 20, "s01", 20, 1);
insert into mst_ticket VALUES (21, 21, "s01", 21, 1);

SELECT * FROM mst_ticket

-- RV-01 予約情報新規登録
insert into tbl_reservation VALUES (
    1, 1, 1
);

-- RV-02
insert into tbl_reservation VALUES (
    2, 1, 1
);

-- RE-01 -RE-05 レビュー新規追加
insert into mst_review VALUES (1, 1, 1, "1", "タイトル", "本文");
insert into mst_review VALUES (2, 1, 1, "2", "タイトル2", "本文2");
insert into mst_review VALUES (3, 1, 1, "3", "タイトル3", "本文3");
insert into mst_review VALUES (4, 1, 1, "4", "タイトル4", "本文4");
insert into mst_review VALUES (5, 1, 1, "5", "タイトル5", "本文5");
